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

  def __set_background_image(self, image_name):
    asset_handler: AssetHandler = AssetHandler()

    try:
      pixmap = asset_handler.get_image(image_name)
      scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatioByExpanding, Qt.SmoothTransformation)
      self.background_label.setPixmap(scaled_pixmap)
      self.background_label.setGeometry(self.rect())

    except FileNotFoundError as e:
      print(e)