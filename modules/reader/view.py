import cv2
import os
import face_recognition
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
    self.student_faces = []

  def init_ui(self):
    self.main_layout = QVBoxLayout()
    center_layout = QVBoxLayout()
    h_center_layout = QHBoxLayout()
    webcam_center_layout = QHBoxLayout()

    top_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    left_spacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)
    right_spacer = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)