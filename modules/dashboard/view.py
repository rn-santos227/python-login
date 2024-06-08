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

    dashboard_button = Button("Dashboard")

    students_button = Button("Students")

    logs_button = Button("Attendance Logs")

    parents_button = Button("Parents")

    self.navigation_menu.addWidget(dashboard_button)
    self.navigation_menu.addWidget(students_button)
    self.navigation_menu.addWidget(logs_button)
    self.navigation_menu.addWidget(parents_button)
    self.navigation_menu.addStretch()