import sys

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem, QSizePolicy
from components.text_field import TextField

class LoginPage(QWidget):
  def __init__(self, main_window):
    super().__init__()
    self.main_window = main_window
    self.init_ui()

  def init_ui(self):
    layout = QVBoxLayout()

    top_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
    bottom_spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

    self.username_field = TextField(label_text="Email", placeholder_text="Enter your username")
    self.password_field = TextField(label_text="Password", placeholder_text="Enter your password")

    self.password_field.text_field.setEchoMode(QLineEdit.Password)

    login_button = QPushButton("Login")
    login_button.clicked.connect(self.handle_login)

    layout.addItem(top_spacer)
    layout.addWidget(QLabel("Login Page"))
    layout.addWidget(self.username_field)
    layout.addWidget(self.password_field)
    layout.addItem(bottom_spacer)