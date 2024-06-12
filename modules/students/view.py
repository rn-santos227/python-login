import modules.students.controller as student_controller

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView,  QSpacerItem, QSizePolicy, QGridLayout

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
    top_layout = QHBoxLayout()
    button_layout = QHBoxLayout()

    create_layout = QGridLayout()

    self.email_field = TextField(label_text="Email", placeholder_text="Enter student email.")
    self.password_field = TextField(label_text="Password", placeholder_text="Enter student password.")
    self.password_field.text_field.setEchoMode(QLineEdit.Password)
    self.fullname_field = TextField(label_text="Full Name", placeholder_text="Enter student full name.")
    self.contact_field = TextField(label_text="Contact Number", placeholder_text="Enter student contact number.")
    self.student_number_field = TextField(label_text="Student Number", placeholder_text="Enter student number.")
    self.section_field = TextField(label_text="Student Section", placeholder_text="Enter student section.")
    self.grade_field = TextField(label_text="Student Grade", placeholder_text="Enter student grade.")

    create_button = Button("Create Student")
    create_button.connect_signal(self.create_student)

    button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    button_layout.addWidget(create_button)

    field_layout_1 = QHBoxLayout()
    field_layout_2 = QHBoxLayout()

    field_layout_1.addWidget(self.contact_field)
    field_layout_1.addWidget(self.student_number_field)

    field_layout_2.addWidget(self.section_field)
    field_layout_2.addWidget(self.grade_field)

    create_layout.addWidget(self.email_field, 0, 0, 1, 2)
    create_layout.addWidget(self.password_field, 1, 0, 1, 2)
    create_layout.addWidget(self.fullname_field, 2, 0, 1, 2)
    create_layout.addLayout(field_layout_1, 3, 0, 1, 2)
    create_layout.addLayout(field_layout_2, 4, 0, 1, 2)
    create_layout.addLayout(button_layout, 5, 0, 1, 2)

    top_layout.addLayout(create_layout)

    self.table_widget = QTableWidget()
    self.table_widget.setColumnCount(8)
    self.table_widget.setHorizontalHeaderLabels(["ID", "Full Name", "Email", "Student Number", "Contact Number", "Section", "Grade", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    main_layout.addLayout(top_layout)
    main_layout.addWidget(self.table_widget)
  
    self.setLayout(main_layout)
    self.load_students()
    
  def init_create_layout(self):
    create_layout = QGridLayout()
    field_layout_1 = QHBoxLayout()
    field_layout_2 = QHBoxLayout()
    self.button_layout = QHBoxLayout()

    self.email_field = TextField(label_text="Email", placeholder_text="Enter student email.")
    self.password_field = TextField(label_text="Password", placeholder_text="Enter student password.")
    self.password_field.text_field.setEchoMode(QLineEdit.Password)
    self.fullname_field = TextField(label_text="Full Name", placeholder_text="Enter student full name.")
    self.contact_field = TextField(label_text="Contact Number", placeholder_text="Enter student contact number.")
    self.student_number_field = TextField(label_text="Student Number", placeholder_text="Enter student number.")
    self.section_field = TextField(label_text="Student Section", placeholder_text="Enter student section.")
    self.grade_field = TextField(label_text="Student Grade", placeholder_text="Enter student grade.")

    create_button = Button("Create Student")
    create_button.connect_signal(self.create_student)

    self.button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    self.button_layout.addWidget(create_button)

    return create_layout

  def create_student(self):
    email = self.email_field.get_text()
    password = self.password_field.get_text()
    full_name = self.fullname_field.get_text()
    contact_number = self.contact_field.get_text()
    student_number = self.student_number_field.get_text()
    section = self.section_field.get_text()
    grade =  self.grade_field.get_text()

    fields_to_validate = [
      (self.validation_handler.is_valid_email, email, "Invalid email address."),
      (self.validation_handler.is_not_empty, password, "Password cannot be empty."),
      (self.validation_handler.is_not_empty, full_name, "Full name cannot be empty."),
      (self.validation_handler.is_not_empty, contact_number, "Contact number cannot be empty."),
      (self.validation_handler.is_not_empty, student_number, "Student number cannot be empty."),
      (self.validation_handler.is_not_empty, section, "Section cannot be empty."),
      (self.validation_handler.is_not_empty, grade, "Grade cannot be empty.")
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
      grade = grade,
      status = "active"
    )

    student_controller.create_student(new_student)
    self.load_students()
    self._clear_fields()
    self.message_box.show_message("Success", "Student has been created successfully.", "Information")

  def load_students(self):
    self.students = student_controller.get_students("status = 'active'", "select")
    self.table_widget.setRowCount(0)

    if not self.students:
      return

    for student in self.students:
      row_position = self.table_widget.rowCount()
      self.table_widget.insertRow(row_position)

      self.table_widget.setItem(row_position, 0, QTableWidgetItem(str(student.id)))
      self.table_widget.setItem(row_position, 1, QTableWidgetItem(student.full_name))
      self.table_widget.setItem(row_position, 2, QTableWidgetItem(student.email))
      self.table_widget.setItem(row_position, 3, QTableWidgetItem(student.student_number))
      self.table_widget.setItem(row_position, 4, QTableWidgetItem(student.contact_number))
      self.table_widget.setItem(row_position, 5, QTableWidgetItem(student.section))
      self.table_widget.setItem(row_position, 6, QTableWidgetItem(student.grade))

      update_button = QPushButton("Update")
      delete_button = QPushButton("Delete")
      
      button_layout = QHBoxLayout()
      button_layout.addWidget(update_button)
      button_layout.addWidget(delete_button)
      button_layout.setContentsMargins(0, 0, 0, 0)
      
      button_widget = QWidget()
      button_widget.setLayout(button_layout)
      
      self.table_widget.setCellWidget(row_position, 7, button_widget)

  def _clear_fields(self):
    self.email_field.clear_text()
    self.password_field.clear_text()
    self.fullname_field.clear_text()
    self.contact_field.clear_text()
    self.student_number_field.clear_text()
    self.section_field.clear_text()
    self.grade_field.clear_text()