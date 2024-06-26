from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from components.title_bar import TitleBar
from handlers.pages_handler import PagesHandler

from modules.auth.view import LoginPage
from modules.dashboard.view import DashboardAdminPage

class ScreenWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowFlags(Qt.FramelessWindowHint)
    self.showFullScreen()

    self.central_widget = QWidget(self)
    self.setCentralWidget(self.central_widget)
    self.layout = QVBoxLayout(self.central_widget)
    self.layout.setContentsMargins(0, 0, 0, 0)
    self.layout.setSpacing(0)

    self.title_bar = TitleBar(self)
    self.layout.addWidget(self.title_bar)

    self.stacked_widget = QStackedWidget()
    self.layout.addWidget(self.stacked_widget)

    self.pages_handler = PagesHandler(self.stacked_widget)

    self.stacked_widget.addWidget(self.pages_handler.login_page)
    self.stacked_widget.addWidget(self.pages_handler.dashboard_page)

    self.pages_handler.switch_to_login_page()

  def keyPressEvent(self, event):
    if event.key() == Qt.Key_Escape:
      pass
