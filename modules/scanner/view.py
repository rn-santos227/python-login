import cv2
import face_recognition
import json
import numpy as np

import modules.students.controller as students_controller

from PyQt5.QtWidgets import QFrame, QHBoxLayout, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget

from components.button import Button
from components.combo_box import ComboBox
from components.message_box import MessageBox
from components.webcam import Webcam

from modules.students.model import Student

from assets.styles.styles import content_frame_style

class ScannerPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.setStyleSheet(content_frame_style)
    self.pages_handler = pages_handler
    self.message_box = MessageBox(self)
    self.students: list[Student] = []
    self.init_ui()

  def init_ui(self):
    content_frame: QFrame = QFrame(self)
    
    self.main_layout: QVBoxLayout = QVBoxLayout()
    center_layout: QVBoxLayout = QVBoxLayout()
    h_center_layout: QHBoxLayout = QHBoxLayout()
    webcam_center_layout: QHBoxLayout = QHBoxLayout()

    top_spacer: QSpacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    bottom_spacer: QSpacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    left_spacer: QSpacerItem = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
    right_spacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

    self.student_combo_box: ComboBox = ComboBox(label_text="Student Names")
    self.items=self.load_students_to_combo_box()
    
    self.webcam_component: Webcam = Webcam(self)

    webcam_center_layout.addItem(left_spacer)
    webcam_center_layout.addWidget(self.webcam_component)
    webcam_center_layout.addItem(right_spacer)

    self.webcam_button: Button = Button("Start Webcam")
    self.webcam_button.connect_signal(self.__enable_capture)

    self.capture_button: Button = Button("Save Face")
    self.capture_button.connect_signal(self.save_face)

    center_layout.addWidget(self.student_combo_box)
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

  def load_students_to_combo_box(self):
    self.students = students_controller.get_students("status = 'active'", "select")

    if not self.students:
      return
    
    items = [(student.full_name, student.id) for student in self.students]
    self.student_combo_box.set_items(items)
  
  def save_face(self):
    ret, frame = self.webcam_component.capture_image()
    if ret:
      student_id = self.student_combo_box.get_selected_value()

      if not student_id:
        self.message_box.show_message("Validation Error", "Name cannot be empty", "error")
        return
      
      student = students_controller.get_student_by_id(student_id)
      image_rgb  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

      image_array = np.array(image_rgb , dtype=np.uint8)
      face_locations = face_recognition.face_locations(image_array)
      face_encodings = face_recognition.face_encodings(image_array, face_locations)

      if face_encodings:
        face_encode = face_encodings[0]
        student.face_encode = json.dumps(face_encode.tolist())

        students_controller.add_face_encode(student=student)
        self.message_box.show_message("Success", f"Face has been captured and saved to database.", "Information")
  
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