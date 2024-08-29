from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog, QFrame, QGraphicsDropShadowEffect, QHeaderView, QSpacerItem, QVBoxLayout, QWidget

from components.message_box import MessageBox

from modules.biometrics.model import Biometric

from assets.styles.styles import content_frame_style

class BiometricsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.setStyleSheet(content_frame_style)
    self.pages_handler = pages_handler
    self.message_box: MessageBox = MessageBox(self)
    self.students: list[Biometric] = []

  def init_ui(self):
    content_frame: QFrame = QFrame(self)
    content_frame.setObjectName("contentFrame")
    content_layout: QVBoxLayout = QVBoxLayout(content_frame)

    shadow_effect: QGraphicsDropShadowEffect = QGraphicsDropShadowEffect()
    