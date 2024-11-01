from PyQt5.QtWidgets import QDialog, QFrame, QHBoxLayout, QLabel, QStackedWidget, QVBoxLayout, QWidget
from PyQt5.QtCore import Qt

from components.button import Button
from components.question_dialog import QuestionDialog

from modules.logs.view import LogsPage

from handlers.asset_handler import AssetHandler
from handlers.session_handler import SessionHandler

class DashboardStudentPage(QWidget):
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

    self.navigation_menu: QVBoxLayout = QVBoxLayout()
    self.left_layout: QVBoxLayout = QVBoxLayout()
    self.main_content: QStackedWidget = QStackedWidget()

    logs_button: Button = Button("Attendance Logs")
    logs_button.connect_signal(self.handle_logs)
    logs_button.set_fixed_width(250)

    self.navigation_menu.addWidget(logs_button)

    main_content_frame: QFrame = QFrame(self)
    main_content_frame.setObjectName("formFrame")

    self.main_content.addWidget(self.logs_content)

  def handle_logs(self):
    self.logs_content.load_logs()
    self.main_content.setCurrentWidget(self.logs_content)

  def handle_logout(self):
    question_box: QuestionDialog = QuestionDialog(message="Are you sure you want to log out?")
    if question_box.exec() == QDialog.Accepted:
      self.session_handler.destroy_session()

  def resizeEvent(self, event):
    super().resizeEvent(event)

  def __set_background_image(self, image_name):
    asset_handler: AssetHandler = AssetHandler()
    self.background_label.setGeometry(self.rect())

    try:
      pixmap = asset_handler.get_image(image_name)
      scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
      self.background_label.setPixmap(scaled_pixmap)
      self.background_label.setGeometry(self.rect())

    except FileNotFoundError as e:
      print(e)