import sys
import os
import face_recognition
import modules.students.controller as student_controller

from PyQt5 import QtCore, QtGui
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy

from components.button import Button
from components.combo_box import ComboBox
from components.message_box import MessageBox
from components.webcam import Webcam

class ScannerPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
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

    self.student_combo_box = ComboBox(label_text="Student Names", items=self.load_students_to_combo_box())
    self.webcam_component = Webcam(self)

    webcam_center_layout.addItem(left_spacer)
    webcam_center_layout.addWidget(self.webcam_component)
    webcam_center_layout.addItem(right_spacer)

    self.webcam_button = Button("Start Webcam")
    self.webcam_button.connect_signal(self.__enable_capture)

    self.capture_button = Button("Capture Face")

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
    students = student_controller.get_students("status = 'active'", "select")
    if not students:
      return
    
    return [(student.full_name, student.id) for student in students]
  
  def save_face(self):
    ret, frame = self.webcam_component.capture_image()
    if ret:
      file_name = self.student_combo_box.get_selected_value()
  
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