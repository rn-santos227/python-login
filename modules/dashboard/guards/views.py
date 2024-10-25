from PyQt5.QtWidgets import QDialog, QFrame, QHBoxLayout, QLabel, QStackedWidget, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from components.button import Button
from components.question_dialog import QuestionDialog

from handlers.asset_handler import AssetHandler
from handlers.session_handler import SessionHandler

class DashboardGuardPage(QWidget):
  def __init__(self, pages_handler, session_handler: SessionHandler):
    super().__init__()
    self.pages_handler = pages_handler
    self.session_handler: SessionHandler = session_handler
    self.navigation_visible = True
    self.__init_ui()

  def __init_ui(self):
    button_bg_color = "#fff6f6"
    button_font_color = "#000000"

    main_layout: QHBoxLayout = QHBoxLayout(self)
    main_layout.setContentsMargins(0, 0, 0, 0)