import cv2
import face_recognition
import json
import numpy as np

import modules.students.controller as student_controller

from PyQt5.QtWidgets import QHBoxLayout, QSizePolicy, QSpacerItem, QVBoxLayout, QWidget

from components.button import Button
from components.combo_box import ComboBox
from components.message_box import MessageBox
from components.webcam import Webcam

from modules.students.handler import students

class ScannerPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.message_box = MessageBox(self)
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

    self.student_combo_box = ComboBox(label_text="Student Names", items=self.load_students_to_combo_box())
    self.webcam_component = Webcam(self)

    webcam_center_layout.addItem(left_spacer)
    webcam_center_layout.addWidget(self.webcam_component)
    webcam_center_layout.addItem(right_spacer)

    self.webcam_button = Button("Start Webcam")
    self.webcam_button.connect_signal(self.__enable_capture)

    self.capture_button = Button("Save Face")
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
    if not students:
      return
    
    return [(student.full_name, student.id) for student in students]
  
  def save_face(self):
    ret, frame = self.webcam_component.capture_image()
    if ret:
      student_id = self.student_combo_box.get_selected_value()

      if not student_id:
        self.message_box.show_message("Validation Error", "Name cannot be empty", "error")
        return
      
      student = student_controller.get_student_by_id(student_id)
      image_rgb  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

      image_array = np.array(image_rgb , dtype=np.uint8)
      face_locations = face_recognition.face_locations(image_array)
      face_encodings = face_recognition.face_encodings(image_array, face_locations)

      if face_encodings:
        face_encode = face_encodings[0]
        student.face_encode = json.dumps(face_encode.tolist())

        student_controller.add_face_encode(student=student)
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