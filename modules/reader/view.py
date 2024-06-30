import cv2
import os
import face_recognition

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSpacerItem, QSizePolicy

import modules.students.controller as student_controller

class ReaderPage(QWidget):
  def __init__(self, page_handler):
    super().__init__()