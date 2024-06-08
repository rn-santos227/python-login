from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox

from components.button import Button
from components.text_field import TextField

class StudentPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.init_ui()

  def init_ui(self):
    main_layout = QVBoxLayout()
    top_half_layout = QVBoxLayout()

    create_layout = QVBoxLayout()

    self.email_field = TextField(label_text="Email", placeholder_text="Enter student email.")
    self.password_field = TextField(label_text="Password", placeholder_text="Enter student password.")
    self.password_field.text_field.setEchoMode(QLineEdit.Password)
    self.fullname_field = TextField(label_text="Full Name", placeholder_text="Enter student full name.")
    self.student_number_field = TextField(label_text="Student Number", placeholder_text="Enter student number.")
    self.section_field = TextField(label_text="Student Section", placeholder_text="Enter student section.")
    self.level_field = TextField(label_text="Student Level", placeholder_text="Enter student level.")


    create_layout.addWidget(self.email_field)
    create_layout.addWidget(self.password_field)
    create_layout.addWidget(self.fullname_field)
    create_layout.addWidget(self.student_number_field)
    create_layout.addWidget(self.section_field)
    create_layout.addWidget(self.level_field)

    top_half_layout.addLayout(create_layout)

    main_layout.addLayout(top_half_layout)
  
    self.setLayout(main_layout)
    