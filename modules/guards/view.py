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