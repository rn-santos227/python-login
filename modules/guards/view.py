import modules.guards.controller as guards_controller

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog, QFrame, QGraphicsDropShadowEffect, QGridLayout, QHeaderView, QHBoxLayout, QLayout, QLayoutItem, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from components.button import Button
from components.message_dialog import MessageDialog
from components.prompt_dialog import PromptDialog
from components.text_field import TextField

from handlers.validations_handler import ValidationHandler

from modules.guards.model import Guard

from assets.styles.styles import content_frame_style

class GuardsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.setStyleSheet(content_frame_style)
    self.pages_handler = pages_handler
    self.message_dialog: MessageDialog = MessageDialog(self)
    self.validation_handler: ValidationHandler = ValidationHandler()
    self.guards: list[Guard] = []

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
    
    self.top_layout: QHBoxLayout = QHBoxLayout()

    self.top_layout.setContentsMargins(150, 0, 150, 20)

  
  def init_create_layout(self):
    create_layout: QGridLayout = QGridLayout()
    self.create_button_layout: QHBoxLayout = QHBoxLayout()

    self.email_field: TextField = TextField(label_text="Email", placeholder_text="Enter guard email.")
    self.password_field: TextField = TextField(label_text="Password", placeholder_text="Enter admin password.")
    self.password_field.text_field.setEchoMode(QLineEdit.Password)
    self.fullname_field: TextField = TextField(label_text="Full Name", placeholder_text="Enter admin full name.")