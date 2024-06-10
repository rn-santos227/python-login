import modules.students.controller as student_controller

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox,  QSpacerItem, QSizePolicy

from components.button import Button
from components.message_box import MessageBox
from components.text_field import TextField

from handlers.validations_handler import ValidationHandler
from modules.students.model import Student

class StudentPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.message_box = MessageBox(self)
    self.validation_handler = ValidationHandler()
    self.students = []
    self.init_ui()

  def init_ui(self):
    main_layout = QVBoxLayout()
    top_half_layout = QVBoxLayout()
    button_layout = QHBoxLayout()

    create_layout = QVBoxLayout()

    self.email_field = TextField(label_text="Email", placeholder_text="Enter student email.")
    self.password_field = TextField(label_text="Password", placeholder_text="Enter student password.")
    self.password_field.text_field.setEchoMode(QLineEdit.Password)
    self.fullname_field = TextField(label_text="Full Name", placeholder_text="Enter student full name.")
    self.contact_field = TextField(label_text="Contact Number", placeholder_text="Enter student contact number.")
    self.student_number_field = TextField(label_text="Student Number", placeholder_text="Enter student number.")
    self.section_field = TextField(label_text="Student Section", placeholder_text="Enter student section.")
    self.level_field = TextField(label_text="Student Level", placeholder_text="Enter student level.")

    create_button = Button("Create Student")
    create_button.connect_signal(self.create_student)

    button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    button_layout.addWidget(create_button)

    create_layout.addWidget(self.email_field)
    create_layout.addWidget(self.password_field)
    create_layout.addWidget(self.fullname_field)
    create_layout.addWidget(self.contact_field)
    create_layout.addWidget(self.student_number_field)
    create_layout.addWidget(self.section_field)
    create_layout.addWidget(self.level_field)
    create_layout.addLayout(button_layout)

    top_half_layout.addLayout(create_layout)

    self.table_widget = QTableWidget()
    self.table_widget.setColumnCount(7)
    self.table_widget.setHorizontalHeaderLabels(["ID", "Full Name", "Email", "Student Number", "Section", "Level", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    main_layout.addLayout(top_half_layout)
    main_layout.addWidget(self.table_widget)
  
    self.setLayout(main_layout)
    self.load_students()
    

  def create_student(self):
    email = self.email_field.get_text()
    password = self.password_field.get_text()
    full_name = self.fullname_field.get_text()
    contact_number = self.contact_field.get_text()
    student_number = self.student_number_field.get_text()
    section = self.section_field.get_text()
    level =  self.level_field .get_text()

    fields_to_validate = [
      (self.validation_handler.is_valid_email, email, "Invalid email address."),
      (self.validation_handler.is_not_empty, password, "Password cannot be empty."),
      (self.validation_handler.is_not_empty, full_name, "Full name cannot be empty."),
      (self.validation_handler.is_not_empty, contact_number, "Contact number cannot be empty."),
      (self.validation_handler.is_not_empty, student_number, "Student number cannot be empty."),
      (self.validation_handler.is_not_empty, section, "Section cannot be empty."),
      (self.validation_handler.is_not_empty, level, "Level cannot be empty.")
    ]

    if not self.validation_handler.validate_fields(self, fields_to_validate):
      return
    
    new_student = Student(
      email = email,
      password = password,
      full_name = full_name,
      contact_number = contact_number,
      student_number = student_number,
      section = section,
      level = level
    )

    student_controller.create_student(new_student)
    self.message_box.show_message("Success", "Student created successfully.", "information")

  def load_students(self):
    self.students = student_controller.get_students("status = 'active'", "select")
    for student in self.students:
      row_position = self.table_widget.rowCount()
      self.table_widget.insertRow(row_position)

