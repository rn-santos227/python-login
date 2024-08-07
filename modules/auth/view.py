from PyQt5.QtWidgets import QFrame, QGraphicsDropShadowEffect, QHBoxLayout, QLabel, QLineEdit, QSpacerItem, QSizePolicy, QVBoxLayout, QWidget
from PyQt5.QtGui import QPixmap, QColor
from PyQt5.QtCore import Qt

from components.alert_message import AlertMessage
from components.button import Button
from components.message_box import MessageBox
from components.text_field import TextField

from handlers.asset_handler import AssetHandler

from modules.auth.controller import login

from assets.styles.styles import auth_view_style
class LoginPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.setStyleSheet(auth_view_style)
    self.alert_message: AlertMessage = AlertMessage() 
    self.pages_handler = pages_handler
    self.init_ui()

  def init_ui(self):
    main_layout: QVBoxLayout = QVBoxLayout(self)
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setSpacing(0)

    self.background_label: QLabel = QLabel(self)
    self._set_background_image("bg.jpg")
    self.background_label.setGeometry(self.rect())
    self.background_label.setScaledContents(True)
    self.background_label.lower()

    header_layout: QHBoxLayout = QHBoxLayout()
    logo1_label: QLabel = QLabel(self)
    logo2_label: QLabel = QLabel(self)
    title_label: QLabel = QLabel("LOG IN MODULE", self)

    logo1_pixmap = QPixmap("path_to_logo1.png").scaled(100, 100, Qt.KeepAspectRatio)
    logo2_pixmap = QPixmap("path_to_logo2.png").scaled(100, 100, Qt.KeepAspectRatio)

    
    center_layout: QVBoxLayout = QVBoxLayout()
    h_center_layout: QHBoxLayout = QHBoxLayout()
    button_layout: QHBoxLayout = QHBoxLayout()

    form_frame: QFrame = QFrame(self)
    form_frame.setObjectName("formFrame")
    form_layout: QVBoxLayout = QVBoxLayout(form_frame)

    shadow_effect: QGraphicsDropShadowEffect = QGraphicsDropShadowEffect()
    shadow_effect.setBlurRadius(15)
    shadow_effect.setColor(QColor(0, 0, 0, 160))
    shadow_effect.setOffset(0, 5)
    
    form_frame.setGraphicsEffect(shadow_effect)

    top_spacer: QSpacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    bottom_spacer: QSpacerItem = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    left_spacer: QSpacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
    right_spacer: QSpacerItem = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
    

    self.email_field: TextField = TextField(label_text="Email", placeholder_text="Enter your username")
    self.password_field: TextField = TextField(label_text="Password", placeholder_text="Enter your password")
    self.password_field.text_field.setEchoMode(QLineEdit.Password)

    login_button: Button = Button("Login")
    login_button.connect_signal(self.handle_login)

    button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    button_layout.addWidget(login_button)

    form_layout.addWidget(self.email_field)
    form_layout.addWidget(self.password_field)
    form_layout.addLayout(button_layout)
    form_layout.addWidget(self.alert_message) 

    center_layout.addWidget(form_frame)

    h_center_layout.addItem(left_spacer)
    h_center_layout.addLayout(center_layout)
    h_center_layout.addItem(right_spacer)

    main_layout.addItem(top_spacer)
    main_layout.addLayout(h_center_layout)
    main_layout.addItem(bottom_spacer)

    self.setLayout(main_layout)

    self.message_box: MessageBox = MessageBox(self)

    self.background_label.lower()
    main_layout.setContentsMargins(0, 0, 0, 0)

    login_button.set_color(bg_color="green", font_color="white")

  def _set_background_image(self, image_name):
    asset_handler: AssetHandler = AssetHandler()

    try:
      pixmap = asset_handler.get_image(image_name)
      self.background_label.setPixmap(pixmap)

    except FileNotFoundError as e:
      print(e)

  def resizeEvent(self, event):
    super().resizeEvent(event)
    self.background_label.setGeometry(self.rect())

  def handle_login(self):
    email = self.email_field.get_text()
    password = self.password_field.get_text()

    if(login(email, password)):
      print("Login Success.")
      self.password_field.clear_text()
      self.email_field.clear_text()
      self.message_box.show_message(title="Information", message="Login Successful.")
      self.pages_handler.switch_to_dashboard_page()

    else:
      print("Login Unsuccessful.")
      self.alert_message.set_message("Invalid username or password")
      self.alert_message.set_alert_type("error")
