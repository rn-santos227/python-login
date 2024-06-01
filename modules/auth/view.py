import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy

from components.button import Button
from components.text_field import TextField

from modules.auth.controller import login

class LoginPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.init_ui()

  def init_ui(self):
    main_layout = QVBoxLayout()
    center_layout = QVBoxLayout()
    h_center_layout = QHBoxLayout()

    top_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    left_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
    right_spacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

    self.email_field = TextField(label_text="Email", placeholder_text="Enter your username")
    self.password_field = TextField(label_text="Password", placeholder_text="Enter your password")
    self.password_field.text_field.setEchoMode(QLineEdit.Password)

    login_button = Button("Login")
    login_button.connect_signal(self.handle_login)

    center_layout.addWidget(self.email_field)
    center_layout.addWidget(self.password_field)
    center_layout.addWidget(login_button)

    h_center_layout.addItem(left_spacer)
    h_center_layout.addLayout(center_layout)
    h_center_layout.addItem(right_spacer)

    main_layout.addItem(top_spacer)
    main_layout.addLayout(h_center_layout)
    main_layout.addItem(bottom_spacer)

    self.setLayout(main_layout)

  def handle_login(self):
    email = self.email_field.get_text()
    password = self.password_field.get_text()

    if(login(email, password)):
      print("Login Success.")

    else:
      print("Login Unsuccessful.")
