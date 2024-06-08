from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
from PyQt5.QtCore import Qt

from components.button import Button

class DashboardPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.init_ui()

  def init_ui(self):
    layout = QHBoxLayout(self)

    self.navigation_menu = QVBoxLayout()
    self.main_content = QStackedWidget()

    logs_button = Button("Attendance Logs")
    students_button = Button("Students")
    parents_button = Button("Parents")
    
    logout_button = Button("Log Out")
    logout_button.connect_signal(self.handle_logout)

    self.navigation_menu.addWidget(logs_button)
    self.navigation_menu.addWidget(students_button)
    self.navigation_menu.addWidget(parents_button)
    self.navigation_menu.addWidget(logout_button)
    self.navigation_menu.addStretch()

    layout.addLayout(self.navigation_menu)
    
    self.setLayout(layout)

  def handle_logout(self):
    self.pages_handler.switch_to_login_page()