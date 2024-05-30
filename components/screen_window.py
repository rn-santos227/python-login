from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow, QStackedWidget
from PyQt5.QtCore import Qt

from handlers.pages_handler import PagesHandler

from modules.auth.view import LoginPage

class ScreenWindow(QMainWindow):
  def __init__(self):
    super().__init__()

    self.setWindowFlags(Qt.FramelessWindowHint)
    self.showFullScreen()

    self.stacked_widget = QStackedWidget()
    self.setCentralWidget(self.stacked_widget)

    self.page_handler = PagesHandler(self.stacked_widget, None)

    self.login_page = LoginPage(self.pages_handler)

    self.stacked_widget.addWidget(self.login_page)


