from PyQt5.QtWidgets import QDialog, QFrame, QGraphicsDropShadowEffect, QHBoxLayout, QLabel, QStackedWidget, QVBoxLayout, QWidget
from PyQt5.QtGui import QColor 
from PyQt5.QtCore import Qt

from components.button import Button
from components.question_box import QuestionBox

from modules.admin.view import AdminsPage
from modules.logs.view import LogsPage
from modules.parents.view import ParentsPage
from modules.reader.view import ReaderPage
from modules.scanner.view import ScannerPage
from modules.students.view import StudentPage

from handlers.asset_handler import AssetHandler

from assets.styles.styles import admin_dashboard_style

class DashboardAdminPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.setStyleSheet(admin_dashboard_style)
    self.pages_handler = pages_handler
    self.navigation_visible = True
    self.init_ui()

  def init_ui(self):
    main_layout: QHBoxLayout = QHBoxLayout(self)
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setSpacing(0)

    self.background_label: QLabel = QLabel(self)
    self.__set_background_image("bg.jpg")
    self.background_label.setScaledContents(True)
    
    self.admins_content: AdminsPage = AdminsPage(self)
    self.logs_content: LogsPage = LogsPage(self)
    self.parents_content: ParentsPage = ParentsPage(self)
    self.reader_content: ReaderPage = ReaderPage(self)
    self.scanner_content: ScannerPage = ScannerPage(self)
    self.students_content: StudentPage = StudentPage(self)

    self.navigation_menu: QVBoxLayout = QVBoxLayout()
    self.left_layout: QVBoxLayout = QVBoxLayout()
    self.main_content: QStackedWidget = QStackedWidget()

    logs_button: Button = Button("Attendance Logs")
    logs_button.connect_signal(self.handle_logs)
    logs_button.set_fixed_width(250)

    reader_button: Button = Button("Read Biometrics")
    reader_button.connect_signal(self.handle_reader)
    reader_button.set_fixed_width(250)
    
    scanner_button: Button = Button("Save Biometrics")
    scanner_button.connect_signal(self.handle_scanner)
    scanner_button.set_fixed_width(250)
    
    students_button: Button = Button("Students")
    students_button.connect_signal(self.handle_students)
    students_button.set_fixed_width(250)

    parents_button: Button = Button("Parents")
    parents_button.connect_signal(self.handle_parents)
    parents_button.set_fixed_width(250)

    users_button: Button = Button("Admin Users")
    users_button.connect_signal(self.handle_admins)
    users_button.set_fixed_width(250)
    
    logout_button: Button = Button("Log Out")
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

    main_content_frame: QFrame = QFrame(self)
    main_content_frame.setObjectName("formFrame")

    shadow_effect: QGraphicsDropShadowEffect = QGraphicsDropShadowEffect()
    shadow_effect.setBlurRadius(15)
    

    self.main_content.addWidget(self.admins_content)
    self.main_content.addWidget(self.logs_content)
    self.main_content.addWidget(self.parents_content)
    self.main_content.addWidget(self.reader_content)
    self.main_content.addWidget(self.scanner_content)
    self.main_content.addWidget(self.students_content)

    self.toggle_button: Button = Button("Toggle Navigation")
    self.toggle_button.connect_signal(self.__toggle_navigation)
    self.toggle_button.set_fixed_width(250)
    
    self.left_layout.addWidget(self.toggle_button)
    self.left_layout.addLayout(self.navigation_menu)

    main_layout.addLayout(self.left_layout, 1)
    main_layout.addWidget(self.main_content, 9)
    
    self.setLayout(main_layout)
    self.handle_logs()

    self.background_label.lower()
    main_layout.setContentsMargins(0, 0, 0, 0)

    logs_button.set_color(bg_color="cyan", font_color="black")
    reader_button.set_color(bg_color="cyan", font_color="black")
    scanner_button.set_color(bg_color="cyan", font_color="black")
    students_button.set_color(bg_color="cyan", font_color="black")
    parents_button.set_color(bg_color="cyan", font_color="black")
    users_button.set_color(bg_color="cyan", font_color="black")
    logout_button.set_color(bg_color="cyan", font_color="black")

  def handle_admins(self):
    self.reader_content.clock_component.start_clock()
    self.admins_content.load_admins()
    self.main_content.setCurrentWidget(self.admins_content)

  def handle_reader(self):
    self.reader_content.clock_component.start_clock()
    self.reader_content.load_logs()
    self.main_content.setCurrentWidget(self.reader_content)

  def handle_scanner(self):
    self.reader_content.clock_component.stop_clock()
    self.scanner_content.load_students_to_combo_box()
    self.main_content.setCurrentWidget(self.scanner_content)

  def handle_students(self):
    self.reader_content.clock_component.stop_clock()
    self.students_content.load_students()
    self.main_content.setCurrentWidget(self.students_content)

  def handle_parents(self):
    self.reader_content.clock_component.stop_clock()
    self.parents_content.load_students_to_combo_box()
    self.parents_content.load_parents()
    self.main_content.setCurrentWidget(self.parents_content)

  def handle_logs(self):
    self.reader_content.clock_component.stop_clock()
    self.logs_content.load_logs()
    self.main_content.setCurrentWidget(self.logs_content)

  def handle_logout(self):
    question_box: QuestionBox = QuestionBox(message="Are you sure you want to log out?")
    if question_box.exec() == QDialog.Accepted:
      self.reader_content.clock_component.stop_clock()
      self.pages_handler.switch_to_login_page()

  def resizeEvent(self, event):
    super().resizeEvent(event)
    self.background_label.setGeometry(self.rect())

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

  def __set_background_image(self, image_name):
    asset_handler: AssetHandler = AssetHandler()

    try:
      pixmap = asset_handler.get_image(image_name)
      scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
      self.background_label.setPixmap(scaled_pixmap)
      self.background_label.setGeometry(self.rect())

    except FileNotFoundError as e:
      print(e)
      

class DashboardStudentPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler