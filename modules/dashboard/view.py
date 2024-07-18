from PyQt5.QtWidgets import QDialog, QHBoxLayout, QStackedWidget, QVBoxLayout, QWidget

from components.button import Button
from components.question_box import QuestionBox

from modules.admin.view import AdminsPage
from modules.logs.view import LogsPage
from modules.parents.view import ParentsPage
from modules.reader.view import ReaderPage
from modules.scanner.view import ScannerPage
from modules.students.view import StudentPage

class DashboardAdminPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.navigation_visible = True
    self.init_ui()

  def init_ui(self):
    self.admins_content = AdminsPage(self)
    self.logs_content = LogsPage(self)
    self.parents_content = ParentsPage(self)
    self.reader_content = ReaderPage(self)
    self.scanner_content = ScannerPage(self)
    self.students_content = StudentPage(self)

    layout = QHBoxLayout(self)

    self.navigation_menu = QVBoxLayout()
    self.left_layout = QVBoxLayout()
    self.main_content = QStackedWidget()

    logs_button = Button("Attendance Logs")
    logs_button.connect_signal(self.handle_logs)
    logs_button.set_fixed_width(250)

    reader_button = Button("Read Biometrics")
    reader_button.connect_signal(self.handle_reader)
    reader_button.set_fixed_width(250)
    
    scanner_button = Button("Save Biometrics")
    scanner_button.connect_signal(self.handle_scanner)
    scanner_button.set_fixed_width(250)
    
    students_button = Button("Students")
    students_button.connect_signal(self.handle_students)
    students_button.set_fixed_width(250)

    parents_button = Button("Parents")
    parents_button.connect_signal(self.handle_parents)
    parents_button.set_fixed_width(250)

    users_button = Button("Admin Users")
    users_button.connect_signal(self.handle_admins)
    users_button.set_fixed_width(250)
    
    logout_button = Button("Log Out")
    logout_button.connect_signal(self.handle_logout)
    logout_button.set_fixed_width(250)

    self.navigation_menu.addWidget(logs_button)
    self.navigation_menu.addWidget(reader_button)
    self.navigation_menu.addWidget(scanner_button)
    self.navigation_menu.addWidget(students_button)
    self.navigation_menu.addWidget(parents_button)
    self.navigation_menu.addWidget(users_button)
    self.navigation_menu.addWidget(logout_button)
    self.navigation_menu.addStretch()

    self.main_content.addWidget(self.admins_content)
    self.main_content.addWidget(self.logs_content)
    self.main_content.addWidget(self.parents_content)
    self.main_content.addWidget(self.reader_content)
    self.main_content.addWidget(self.scanner_content)
    self.main_content.addWidget(self.students_content)

    self.toggle_button = Button("Toggle Navigation")
    self.toggle_button.connect_signal(self.__toggle_navigation)
    self.toggle_button.set_fixed_width(250)
    
    self.left_layout.addWidget(self.toggle_button)
    self.left_layout.addLayout(self.navigation_menu)

    layout.addLayout(self.left_layout, 1)
    layout.addWidget(self.main_content, 9)
    
    self.setLayout(layout)
    self.handle_logs()

  def handle_admins(self):
    self.main_content.setCurrentWidget(self.admins_content)

  def handle_reader(self):
    self.main_content.setCurrentWidget(self.reader_content)

  def handle_scanner(self):
    self.scanner_content.load_students_to_combo_box()
    self.main_content.setCurrentWidget(self.scanner_content)

  def handle_students(self):
    self.students_content.load_students()
    self.main_content.setCurrentWidget(self.students_content)

  def handle_parents(self):
    self.parents_content.load_students_to_combo_box()
    self.main_content.setCurrentWidget(self.parents_content)

  def handle_logs(self):
    self.main_content.setCurrentWidget(self.logs_content)

  def handle_logout(self):
    question_box = QuestionBox(message="Are you sure you want to log out?")
    if question_box.exec() == QDialog.Accepted:
      self.pages_handler.switch_to_login_page()

  def __toggle_navigation(self):
    if self.navigation_visible:
      self.navigation_visible = False
      for index in reversed(range(self.navigation_menu.count())):
        widget = self.navigation_menu.itemAt(index).widget()
        if widget is not None:
          widget.hide()
    
    else:
      self.navigation_visible = True
      for index in range(self.navigation_menu.count()):
        widget = self.navigation_menu.itemAt(index).widget()
        if widget is not None:
          widget.show()

class DashboardStudentPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler