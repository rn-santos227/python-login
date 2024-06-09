from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QStackedWidget
from PyQt5.QtCore import Qt

from components.button import Button

from modules.students.view import StudentPage

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
    students_button.connect_signal(self.handle_student)

    parents_button = Button("Parents")

    users_button = Button("Admin Users")
    
    logout_button = Button("Log Out")
    logout_button.connect_signal(self.handle_logout)

    self.navigation_menu.addWidget(logs_button)
    self.navigation_menu.addWidget(students_button)
    self.navigation_menu.addWidget(parents_button)
    self.navigation_menu.addWidget(users_button)
    self.navigation_menu.addWidget(logout_button)
    self.navigation_menu.addStretch()

    self.students_content = StudentPage(self)

    self.main_content.addWidget(self.students_content)

    layout.addLayout(self.navigation_menu)
    layout.addWidget(self.main_content)
    
    self.setLayout(layout)

  def handle_student(self):
    self.main_content.setCurrentWidget(self.students_content)

  def handle_logout(self):
    self.pages_handler.switch_to_login_page()