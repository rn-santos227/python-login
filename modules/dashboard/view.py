from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QStackedWidget
from PyQt5.QtCore import Qt

from components.button import Button

from modules.admin.view import AdminsPage
from modules.logs.view import LogsPage
from modules.parents.view import ParentsPage
from modules.scanner.view import ScannerPage
from modules.students.view import StudentPage

class DashboardAdminPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.init_ui()

  def init_ui(self):
    self.admins_content = AdminsPage(self)
    self.logs_content = LogsPage(self)
    self.parents_content = ParentsPage(self)
    self.scanner_content = ScannerPage(self)
    self.students_content = StudentPage(self)

    layout = QHBoxLayout(self)

    self.navigation_menu = QVBoxLayout()
    self.main_content = QStackedWidget()

    logs_button = Button("Attendance Logs")
    logs_button.connect_signal(self.handle_logs)

    scanner_button = Button("Save Biometric")
    scanner_button.connect_signal(self.handle_scanner)
    
    students_button = Button("Students")
    students_button.connect_signal(self.handle_students)

    parents_button = Button("Parents")
    parents_button.connect_signal(self.handle_parents)

    users_button = Button("Admin Users")
    users_button.connect_signal(self.handle_admins)
    
    logout_button = Button("Log Out")
    logout_button.connect_signal(self.handle_logout)

    self.navigation_menu.addWidget(logs_button)
    self.navigation_menu.addWidget(scanner_button)
    self.navigation_menu.addWidget(students_button)
    self.navigation_menu.addWidget(parents_button)
    self.navigation_menu.addWidget(users_button)
    self.navigation_menu.addWidget(logout_button)
    self.navigation_menu.addStretch()

    self.main_content.addWidget(self.admins_content)
    self.main_content.addWidget(self.logs_content)
    self.main_content.addWidget(self.parents_content)
    self.main_content.addWidget(self.students_content)

    layout.addLayout(self.navigation_menu)
    layout.addWidget(self.main_content)
    
    self.setLayout(layout)
    self.handle_logs()

  def handle_admins(self):
    self.main_content.setCurrentWidget(self.admins_content)

  def handle_scanner(self):
    self.main_content.setCurrentWidget(self.scanner_content)

  def handle_students(self):
    self.main_content.setCurrentWidget(self.students_content)

  def handle_parents(self):
    self.main_content.setCurrentWidget(self.parents_content)

  def handle_logs(self):
    self.main_content.setCurrentWidget(self.logs_content)

  def handle_logout(self):
    self.pages_handler.switch_to_login_page()

class DashboardStudentPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler