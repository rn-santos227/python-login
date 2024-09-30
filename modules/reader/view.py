import cv2
import face_recognition
import json
import re
import numpy as np

import modules.logs.controller as logs_controller
import modules.students.controller as students_controller

from datetime import datetime
from PyQt5.QtCore import Qt, QDate, QEvent, QTimer
from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QFrame, QGraphicsDropShadowEffect, QLabel, QHBoxLayout, QSpacerItem, QSizePolicy, QVBoxLayout, QWidget

from components.button import Button
from components.clock import Clock
from components.combo_box import ComboBox
from components.message_box import MessageBox
from components.popup_dialog import PopupDialog
from components.webcam import Webcam

from handlers.biometrics_handler import BiometricsHandler
from handlers.sms_handler import send_sms, compose_message
from handlers.email_handler import send_email

from modules.logs.model import Log
from modules.biometrics.model import Biometric
from modules.students.model import Student
from modules.biometrics.controller import get_biometrics
from modules.parents.controller import get_parents

from threads.capture_thread import CaptureThread

from assets.styles.styles import date_label_style, content_frame_style

class ReaderPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.setStyleSheet(content_frame_style)
    self.pages_handler = pages_handler
    self.biometrics_handler: BiometricsHandler = BiometricsHandler()
    self.capture_thread: CaptureThread = None 
    self.popup_dialog: PopupDialog = PopupDialog(parent=self)
    self.clock_component: Clock = Clock()
    self.message_box: MessageBox = MessageBox(self)
    self.biometrics: list[Biometric] = []
    self.logs: list[Log] = []
    self.students: list[Student] = []
    self.devices = []
    self.__init_ui()

  def __init_ui(self):
    content_frame: QFrame = QFrame(self)
    content_frame.setObjectName("contentFrame")
    content_layout: QVBoxLayout = QVBoxLayout(content_frame)

    shadow_effect: QGraphicsDropShadowEffect = QGraphicsDropShadowEffect()
    shadow_effect.setBlurRadius(15)
    shadow_effect.setColor(QColor(0, 0, 0, 160))
    shadow_effect.setOffset(0, 5)

    content_frame.setGraphicsEffect(shadow_effect)

    self.main_layout: QVBoxLayout = QVBoxLayout()
    webcam_layout: QVBoxLayout = QVBoxLayout()
    clock_layout: QVBoxLayout = QVBoxLayout()

    center_layout: QHBoxLayout = QHBoxLayout()
    h_center_layout: QHBoxLayout = QHBoxLayout()

    top_spacer: QSpacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    bottom_spacer: QSpacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    left_spacer: QSpacerItem = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
    right_spacer: QSpacerItem = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

    self.webcam_component: Webcam = Webcam(self)

    webcam_center_layout: QHBoxLayout = QHBoxLayout()
    webcam_center_layout.addItem(left_spacer)
    webcam_center_layout.addWidget(self.webcam_component)
    webcam_center_layout.addItem(right_spacer)

    self.webcam_button: Button = Button("Start Webcam")
    self.webcam_button.connect_signal(self.__enable_capture)

    self.capture_button: Button = Button("Search Face")
    self.capture_button.connect_signal(self.match_face)

    webcam_layout.addLayout(webcam_center_layout)
    webcam_layout.addWidget(self.webcam_button)
    webcam_layout.addWidget(self.capture_button)

    self.biometrics_combo_box: ComboBox = ComboBox(label_text="Biometrics List")

    self.date_label: QLabel = QLabel(self)
    current_date = QDate.currentDate().toString("dddd, MMMM d, yyyy")
    self.date_label.setText(current_date)
    self.date_label.setAlignment(Qt.AlignCenter)
    self.date_label.setStyleSheet(date_label_style)
    
    clock_center_layout: QHBoxLayout = QHBoxLayout()
    clock_center_layout.addItem(left_spacer)
    clock_center_layout.addWidget(self.clock_component)
    clock_center_layout.addItem(right_spacer)

    clock_layout.addLayout(clock_center_layout)
    clock_layout.addWidget(self.date_label) 

    center_layout.addLayout(clock_layout)
    center_layout.setStretch(0, 1)
    center_layout.addLayout(webcam_layout)
    center_layout.setStretch(1, 1)

    h_center_layout.addLayout(center_layout)

    content_layout.addWidget(self.biometrics_combo_box)
    content_layout.addItem(top_spacer)
    content_layout.addLayout(h_center_layout)
    content_layout.addItem(bottom_spacer)

    self.main_layout.addWidget(content_frame)

    self.setLayout(self.main_layout)
    self.capture_button.set_disabled()

    self.timer = QTimer(self)
    self.timer.timeout.connect(self.update_fingerprint)

  def hideEvent(self, event: QEvent):
    self.stop_scanner()
    super().hideEvent(event)

  def load_logs(self):
    start_date = str(datetime.now().strftime("%Y-%m-%d"))
    end_date = str(datetime.now().strftime("%Y-%m-%d"))

    self.logs = logs_controller.get_logs_with_students(f"date >= '{start_date}' AND date <= '{end_date}'")
    self.students = students_controller.get_students("status = 'active'", "select")
    self.biometrics = get_biometrics("all", "select")

  def load_biometric_devices_to_combo_box(self):
    self.devices.clear()
    self.devices = self.biometrics_handler.get_devices()
    if not self.devices:
      return
    
    pattern = r"\{(.*?)\}"
    items = []

    for device in self.devices:
      match = re.search(pattern, device)
      if match:
        items.append((match.group(1), device))

    self.biometrics_combo_box.set_items(items)
    self.start_scanner()

  def create_log(self, current_date: datetime, student_id: int) -> Log:
    formatted_date = current_date.strftime("%Y-%m-%d")
    log = Log(
      student_id = student_id,
      date = formatted_date
    )

    return logs_controller.create_log(log)

  def get_log(self, current_date: datetime, student_id: int):
    formatted_date = current_date.strftime("%Y-%m-%d")
    return logs_controller.get_log_by_student_and_date(student_id=student_id, date=formatted_date)

  def match_face(self):
    ret, frame = self.webcam_component.capture_image()
    
    if not ret:
      self.message_box.show_message("Error", "No face detected", "error")
      return
    
    image_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image_array = np.array(image_rgb , dtype=np.uint8)
    face_locations = face_recognition.face_locations(image_array)
    face_encodings = face_recognition.face_encodings(image_array, face_locations)
    face_input = np.array(face_encodings[0])

    for student in self.students:
      student_face_encode = student.face_encode
      if not student_face_encode:
        continue
      
      student_face = np.array(json.loads(student_face_encode))
      distance = face_recognition.face_distance([student_face], face_input)

      if distance < 0.6:
        current_date = datetime.now()
        formatted_date_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
        log = self.get_log(current_date, student.id)

        if log is None:
          login = self.create_log(current_date, student.id)
          login.login_time = formatted_date_time
          logs_controller.add_login_time(login)
           
          login_message = compose_message(student=student, time=formatted_date_time, logged="logged in")
          send_sms(contact_number=student.contact_number, message=login_message)
          send_email(student.email, message=login_message)
          self.__send_sms_to_parents(student, message=login_message)

        else:
          if log.logout_time is not None:
            self.message_box.show_message("Information", "Student already logged out.", "information")
            return
          
          log.logout_time = formatted_date_time

          logs_controller.add_logout_time(log)
          logout_message = compose_message(student=student, time=formatted_date_time, logged="logged out")
          send_sms(contact_number=student.contact_number, message=logout_message)
          send_email(student.email, message=logout_message)
          self.__send_sms_to_parents(student, message=logout_message)
        
        self.popup_dialog.set_student(student=student)
        self.popup_dialog.set_logged_time(logged=formatted_date_time)
        self.popup_dialog.show()
        return
      
    self.message_box.show_message("Information", "No match has been found.", "information")

  def start_scanner(self):
    if len(self.devices) > 0:
      device = self.biometrics_combo_box.get_selected_value()

      if device:
        if self.capture_thread and self.capture_thread.isRunning():
          self.stop_scanner()

        self.capture_thread = CaptureThread(self.biometrics_handler, device)
        self.capture_thread.result_ready.connect(self.update_fingerprint)
        self.capture_thread.start()

  def update_fingerprint(self, capture_result):
    img_data, width, height = capture_result
    
    if self.capture_thread:
      fingerprint_data = img_data

      for biometric in self.biometrics:
        result = self.biometrics_handler.verify_fingerprints(fingerprint_data, biometric.fingerprint_data, width, height)
        if result:
          current_date = datetime.now()
          formatted_date_time = current_date.strftime("%Y-%m-%d %H:%M:%S")
          log = self.get_log(current_date, biometric.student_id)

          if log is None:
            login = self.create_log(current_date, biometric.student_id)
          
          return
        
      
      self.message_box.show_message("Information", "No fingerprint match has been found.", "information")

    else:
      self.stop_scanner()

  def stop_scanner(self):
    if len(self.devices) > 0:
      if self.capture_thread:
        print("Stopping scanner...")
        self.capture_thread.stop()
        self.capture_thread = None
        print("Scanner stopped.")

  def __enable_capture(self):
    self.webcam_component.start_webcam()
    self.capture_button.set_enabled()
    self.webcam_button.set_button_text("Stop Webcam")
    self.webcam_button.disconnect_signal(self.__enable_capture)
    self.webcam_button.connect_signal(self.__disable_capture)

  def __disable_capture(self):
    self.webcam_component.stop_webcam()
    self.capture_button.set_disabled()
    self.webcam_button.set_button_text("Start Webcam")
    self.webcam_button.disconnect_signal(self.__disable_capture)
    self.webcam_button.connect_signal(self.__enable_capture)

  def __send_sms_to_parents(self, student: Student, message: str):
    parents = get_parents(f"student_id = {student.id}", "select")
    for parent in parents:
      send_sms(contact_number=parent.contact, message=message)
      send_email(parent.email, message=message)