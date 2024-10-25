from PyQt5.QtWidgets import QDialog, QFrame, QHBoxLayout, QLabel, QStackedWidget, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from handlers.asset_handler import AssetHandler
from handlers.session_handler import SessionHandler

class DashboardGuardPage(QWidget):
  def __init__(self, pages_handler, session_handler: SessionHandler):
    super().__init__()
    self.pages_handler = pages_handler
    self.session_handler: SessionHandler = session_handler
    self.navigation_visible = True

  def __init_ui(self):
    button_bg_color = "#fff6f6"
    button_font_color = "#000000"