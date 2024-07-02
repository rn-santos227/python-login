import cv2
import face_recognition
import numpy as np
import modules.students.controller as student_controller
import modules.logs.controller as log_controller

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy

from components.button import Button
from components.message_box import MessageBox
from components.webcam import Webcam

class ReaderPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.message_box = MessageBox(self)
    self.students = []
    self.init_ui()
    self.load_students()

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

    self.capture_button = Button("Capture Face")

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

  def load_students(self):
    self.students = student_controller.get_students("status = 'active'", "select")

  def match_face(self):
    ret, frame = self.webcam_component.capture_image()
    
    if not ret:
      self.message_box.show_message("Error", "No face detected", "error")
      return
    
    image_rgb  = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    image_array = np.array(image_rgb , dtype=np.uint8)

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