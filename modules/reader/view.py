import cv2
import face_recognition
import json
import numpy as np

import modules.logs.controller as log_controller
import modules.students.controller as students_controller

from datetime import datetime
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy

from components.button import Button
from components.message_box import MessageBox
from components.webcam import Webcam

from handlers.sms_handler import send_sms, compose_message

from modules.logs.model import Log
from modules.students.model import Student

from modules.parents.controller import get_parents

class ReaderPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.message_box = MessageBox(self)
    self.logs = []
    self.students = []
    self.init_ui()

  def init_ui(self):
    self.main_layout = QVBoxLayout()
    center_layout = QVBoxLayout()
    h_center_layout = QHBoxLayout()
    webcam_center_layout = QHBoxLayout()

    top_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    left_spacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
    right_spacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

    self.webcam_component = Webcam(self)

    webcam_center_layout.addItem(left_spacer)
    webcam_center_layout.addWidget(self.webcam_component)
    webcam_center_layout.addItem(right_spacer)

    self.webcam_button = Button("Start Webcam")
    self.webcam_button.connect_signal(self.__enable_capture)

    self.capture_button = Button("Search Face")
    self.capture_button.connect_signal(self.match_face)

    center_layout.addLayout(webcam_center_layout)
    center_layout.addWidget(self.webcam_button)
    center_layout.addWidget(self.capture_button)

    h_center_layout.addItem(left_spacer)
    h_center_layout.addLayout(center_layout)
    h_center_layout.addItem(right_spacer)

    self.main_layout.addItem(top_spacer)
    self.main_layout.addItem(h_center_layout)
    self.main_layout.addItem(bottom_spacer)

    self.setLayout(self.main_layout)
    self.capture_button.set_disabled()

  def load_logs(self):
    start_date = str(datetime.now().strftime("%Y-%m-%d"))

  def match_face(self):
    self.students = students_controller.get_students("status = 'active'", "select")
    ret, frame = self.webcam_component.capture_image()
    
    if not ret:
      self.message_box.show_message("Error", "No face detected", "error")
      return
    
    image_rgb  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
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
        formatted_date = current_date.strftime("%m/%d/%Y")
        formatted_date_time = current_date.strftime("%m/%d/%Y %I:%M:%S %p")
        log = log_controller.get_log_by_student_and_date(student_id=student.id, date=formatted_date)
        
        if log is None:
          log = Log(
            student_id = student.id,
            date = formatted_date
          )

          login = log_controller.create_log(log)
          login.login_time = formatted_date_time
          log_controller.add_login_time(login)
          self.message_box.show_message("Information", f"Student: {student.full_name} has logged in on {formatted_date_time}", "information")
          login_message = compose_message(student=student, time=formatted_date_time, logged="logged in")
          send_sms(contact_number=student.contact_number, message=login_message)
          self.__send_sms_to_parents(student=student, time=formatted_date_time, logged="logged in")

        else:
          if log.logout_time is not None:
            self.message_box.show_message("Information", "Student already logged out.", "information")
            return
          
          log.logout_time = formatted_date_time
          log_controller.add_logout_time(log)
          self.message_box.show_message("Information", f"Student: {student.full_name} has logged out on {formatted_date_time}", "information")
          logout_message = compose_message(student=student, time=formatted_date_time, logged="logged out")
          send_sms(contact_number=student.contact_number, message=logout_message)
          self.__send_sms_to_parents(student=student, time=formatted_date_time, logged="logged out")

        return
      
    self.message_box.show_message("Information", "No match has been found.", "information")

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


  def __send_sms_to_parents(student: Student, time: str, logged: str):
    parents = get_parents(f"student_id = {student.id}", "select")
    for parent in parents:
      message = compose_message(student=student, time=time, logged=logged)
      send_sms(contact_number=parent.contact, message=message)