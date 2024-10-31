from PyQt5.QtWidgets import QDialog, QFrame, QHBoxLayout, QLabel, QStackedWidget, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from handlers.asset_handler import AssetHandler
from handlers.session_handler import SessionHandler

class DashboardStudentPage(QWidget):
  def __init__(self, pages_handler, session_handler: SessionHandler):
    super().__init__()
    self.pages_handler = pages_handler
    self.session_handler: SessionHandler = session_handler