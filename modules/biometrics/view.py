from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog, QFrame, QGraphicsDropShadowEffect, QHBoxLayout, QGridLayout, QSpacerItem, QVBoxLayout, QWidget

from components.button import Button
from components.combo_box import ComboBox
from components.message_box import MessageBox

from modules.biometrics.model import Biometric
from modules.students.model import Student

from assets.styles.styles import content_frame_style

class BiometricsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.setStyleSheet(content_frame_style)
    self.pages_handler = pages_handler
    self.message_box: MessageBox = MessageBox(self)
    self.biometrics: list[Biometric] = []
    self.students: list[Student] = []

  def init_ui(self):
    content_frame: QFrame = QFrame(self)
    content_frame.setObjectName("contentFrame")
    content_layout: QVBoxLayout = QVBoxLayout(content_frame)

    shadow_effect: QGraphicsDropShadowEffect = QGraphicsDropShadowEffect()
    shadow_effect.setBlurRadius(15)
    shadow_effect.setColor(QColor(0, 0, 0, 160))
    shadow_effect.setOffset(0, 5)

    content_frame.setGraphicsEffect(shadow_effect)
    
    self.main_layout: QVBoxLayout = QVBoxLayout()
    left_content_layout: QVBoxLayout = QVBoxLayout()
    right_content_layout: QVBoxLayout = QVBoxLayout()

    self.student_combo_box: ComboBox = ComboBox(label_text="Student Names")

  def load_students_to_combo_box(self):
    pass
    
    