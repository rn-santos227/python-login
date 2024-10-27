from PyQt5.QtWidgets import QDialog, QFrame, QHBoxLayout, QLabel, QStackedWidget, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from components.button import Button
from components.question_dialog import QuestionDialog

from modules.logs.view import LogsPage
from modules.reader.view import ReaderPage

from handlers.asset_handler import AssetHandler
from handlers.session_handler import SessionHandler

class DashboardGuardPage(QWidget):
  def __init__(self, pages_handler, session_handler: SessionHandler):
    super().__init__()
    self.pages_handler = pages_handler
    self.session_handler: SessionHandler = session_handler
    self.navigation_visible = True
    self.__init_ui()

  def __init_ui(self):
    button_bg_color = "#fff6f6"
    button_font_color = "#000000"

    main_layout: QHBoxLayout = QHBoxLayout(self)
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setSpacing(0)

    self.background_label: QLabel = QLabel(self)
    self.__set_background_image("bg.jpg")
    self.background_label.setScaledContents(True)

    self.logs_content: LogsPage = LogsPage(self)
    self.reader_content: ReaderPage = ReaderPage(self)

    self.navigation_menu: QVBoxLayout = QVBoxLayout()
    self.left_layout: QVBoxLayout = QVBoxLayout()
    self.main_content: QStackedWidget = QStackedWidget()

    logs_button: Button = Button("Attendance Logs")
    logs_button.connect_signal(self.handle_logs)
    logs_button.set_fixed_width(250)

    reader_button: Button = Button("Attendance Reader")
    reader_button.connect_signal(self.handle_reader)
    reader_button.set_fixed_width(250)

    logout_button: Button = Button("Log Out")
    logout_button.connect_signal(self.handle_logout)
    logout_button.set_fixed_width(250)

    self.navigation_menu.addWidget(logs_button)
    self.navigation_menu.addWidget(reader_button)
    self.navigation_menu.addWidget(logout_button)
    self.navigation_menu.addStretch()

    main_content_frame: QFrame = QFrame(self)
    main_content_frame.setObjectName("formFrame")

    self.main_content.addWidget(self.logs_content)
    self.main_content.addWidget(self.reader_content)

    self.toggle_button: Button = Button("Toggle Navigation")
    self.toggle_button.set_fixed_width(250)

  def handle_reader(self):
    self.reader_content.clock_component.start_clock()
    self.reader_content.load_logs()
    self.reader_content.load_biometric_devices_to_combo_box()
    self.main_content.setCurrentWidget(self.reader_content)

  def handle_logs(self):
    self.reader_content.clock_component.stop_clock()
    self.logs_content.load_logs()
    self.main_content.setCurrentWidget(self.logs_content)

  def handle_logout(self):
    question_box: QuestionDialog = QuestionDialog(message="Are you sure you want to log out?")
    if question_box.exec() == QDialog.Accepted:
      self.reader_content.clock_component.stop_clock()
      self.session_handler.destroy_session()
      self.pages_handler.switch_to_login_page()

  def __toggle_navigation(self):
    if self.navigation_visible:
      self.navigation_visible = False

  def __set_background_image(self, image_name):
    asset_handler: AssetHandler = AssetHandler()

    try:
      pixmap = asset_handler.get_image(image_name)
      scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
      self.background_label.setPixmap(scaled_pixmap)
      self.background_label.setGeometry(self.rect())

    except FileNotFoundError as e:
      print(e)