from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QHBoxLayout, QLineEdit, QSpacerItem, QSizePolicy, QFrame

from components.alert_message import AlertMessage
from components.button import Button
from components.message_box import MessageBox
from components.text_field import TextField

from handlers.asset_handler import AssetHandler

from modules.auth.controller import login

class LoginPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.init_ui()

  def init_ui(self):
    main_layout = QVBoxLayout(self)
    main_layout.setContentsMargins(0, 0, 0, 0)
    main_layout.setSpacing(0)

    self.background_label = QLabel(self)
    self._set_background_image("bg.jpg")
    self.background_label.setGeometry(self.rect())
    self.background_label.setScaledContents(True)
    self.background_label.lower()

    center_layout = QVBoxLayout()
    h_center_layout = QHBoxLayout()
    button_layout = QHBoxLayout()

    form_frame = QFrame(self)
    form_frame.setFrameShape(QFrame.Box)
    form_frame.setFrameShadow(QFrame.Raised)
    form_frame.setStyleSheet("background-color: rgba(255, 255, 255, 220);")
    form_layout = QVBoxLayout(form_frame)

    top_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
    right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
    
    self.alert_message = AlertMessage() 

    self.email_field = TextField(label_text="Email", placeholder_text="Enter your username")
    self.password_field = TextField(label_text="Password", placeholder_text="Enter your password")
    self.password_field.text_field.setEchoMode(QLineEdit.Password)

    login_button = Button("Login")
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

    self.message_box = MessageBox(self)

    self.background_label.lower()
    main_layout.setContentsMargins(0, 0, 0, 0)


  def _set_background_image(self, image_name):
    asset_handler = AssetHandler()

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
