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
    self.main_layout = QVBoxLayout()
    self.top_layout = QHBoxLayout()

    self.top_layout.addLayout(self.init_create_layout())

    self.table_widget = QTableWidget()
    self.table_widget.setColumnCount(8)
    self.table_widget.setHorizontalHeaderLabels(["ID", "Full Name", "Email", "Student Number", "Contact Number", "Section", "Grade", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    self.main_layout.addLayout(self.top_layout)
    self.main_layout.addWidget(self.table_widget)
  
    self.setLayout(self.main_layout)
    self.load_students()
    
  def init_create_layout(self):
    create_layout = QGridLayout()
    field_layout_1 = QHBoxLayout()
    field_layout_2 = QHBoxLayout()
    self.create_button_layout = QHBoxLayout()

    self.email_field = TextField(label_text="Email", placeholder_text="Enter student email.")
    self.password_field = TextField(label_text="Password", placeholder_text="Enter student password.")
    self.password_field.text_field.setEchoMode(QLineEdit.Password)
    self.fullname_field = TextField(label_text="Full Name", placeholder_text="Enter student full name.")
    self.contact_field = TextField(label_text="Contact Number", placeholder_text="Enter student contact number.")
    self.student_number_field = TextField(label_text="Student Number", placeholder_text="Enter student number.")
    self.section_field = TextField(label_text="Student Section", placeholder_text="Enter student section.")
    self.grade_field = TextField(label_text="Student Grade", placeholder_text="Enter student grade.")

    field_layout_1.addWidget(self.contact_field)
    field_layout_1.addWidget(self.student_number_field)

    field_layout_2.addWidget(self.section_field)
    field_layout_2.addWidget(self.grade_field)

    create_button = Button("Create Student")
    create_button.connect_signal(self.create_student)

    self.create_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    self.create_button_layout.addWidget(create_button)

    create_layout.addWidget(self.email_field, 0, 0, 1, 2)
    create_layout.addWidget(self.password_field, 1, 0, 1, 2)
    create_layout.addWidget(self.fullname_field, 2, 0, 1, 2)
    create_layout.addLayout(field_layout_1, 3, 0, 1, 2)
    create_layout.addLayout(field_layout_2, 4, 0, 1, 2)
    create_layout.addLayout(self.create_button_layout, 5, 0, 1, 2)

    return create_layout

  def init_update_layout(self):
    update_layout = QGridLayout()

    field_layout_1 = QHBoxLayout()
    field_layout_2 = QHBoxLayout()
    self.update_button_layout = QHBoxLayout()

    self.update_email_field = TextField(label_text="Email", placeholder_text="Enter student email.")
    self.update_password_field = TextField(label_text="Password", placeholder_text="Enter student password.")
    self.update_password_field.text_field.setEchoMode(QLineEdit.Password)
    self.update_fullname_field = TextField(label_text="Full Name", placeholder_text="Enter student full name.")
    self.update_contact_field = TextField(label_text="Contact Number", placeholder_text="Enter student contact number.")
    self.update_student_number_field = TextField(label_text="Student Number", placeholder_text="Enter student number.")
    self.update_section_field = TextField(label_text="Student Section", placeholder_text="Enter student section.")
    self.update_grade_field = TextField(label_text="Student Grade", placeholder_text="Enter student grade.")

    update_button = Button("Update Student")
    
    cancel_button = Button("Cancel Update")
    cancel_button.connect_signal(self._switch_to_create_layout)

    self.update_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    self.update_button_layout.addWidget(update_button)
    self.update_button_layout.addWidget(cancel_button)

    field_layout_1.addWidget(self.update_contact_field)
    field_layout_1.addWidget(self.update_student_number_field)

    field_layout_2.addWidget(self.update_section_field)
    field_layout_2.addWidget(self.update_grade_field)

    update_layout.addWidget(self.update_email_field, 0, 0, 1, 2)
    update_layout.addWidget(self.update_password_field, 1, 0, 1, 2)
    update_layout.addWidget(self.update_fullname_field, 2, 0, 1, 2)
    update_layout.addLayout(field_layout_1, 3, 0, 1, 2)
    update_layout.addLayout(field_layout_2, 4, 0, 1, 2)
    update_layout.addLayout(self.update_button_layout, 5, 0, 1, 2)

    return update_layout

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

  def update_student(self):
    email = self.update_email_field.get_text()
    password = self.update_password_field.get_text()
    full_name = self.update_fullname_field.get_text()
    contact_number = self.update_contact_field.get_text()
    student_number = self.update_student_number_field.get_text()
    section = self.update_section_field.get_text()
    grade = self.update_grade_field.get_text()

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
      update_button.clicked.connect(lambda ch, student=student: self._load_student_for_update(student))

      delete_button = QPushButton("Delete")
      
      button_layout = QHBoxLayout()
      button_layout.addWidget(update_button)
      
      button_layout.addWidget(delete_button)
      button_layout.setContentsMargins(0, 0, 0, 0)
      
      button_widget = QWidget()
      button_widget.setLayout(button_layout)
      
      self.table_widget.setCellWidget(row_position, 7, button_widget)

  def _load_student_for_update(self, student: Student):
    self._switch_to_update_layout()
    self.student_id = student.id

    self.update_email_field.set_text(student.email)
    self.update_fullname_field.set_text(student.full_name)
    self.update_student_number_field.set_text(student.student_number)
    self.update_contact_field.set_text(student.contact_number)
    self.update_section_field.set_text(student.section)
    self.update_grade_field.set_text(student.grade)
    
  def _switch_to_update_layout(self):
    while self.top_layout.count():
      child = self.top_layout.takeAt(0)
      if child.widget():
        child.widget().deleteLater()
      elif child.layout():
        self._clear_layout(child.layout())
    self.top_layout.addLayout(self.init_update_layout())

  def _switch_to_create_layout(self):
    while self.top_layout.count():
      child = self.top_layout.takeAt(0)
      if child.widget():
        child.widget().deleteLater()
      elif child.layout():
        self._clear_layout(child.layout())
    self.top_layout.addLayout(self.init_create_layout())
    self._clear_fields()

  def _clear_fields(self):
    self.email_field.clear_text()
    self.password_field.clear_text()
    self.fullname_field.clear_text()
    self.contact_field.clear_text()
    self.student_number_field.clear_text()
    self.section_field.clear_text()
    self.grade_field.clear_text()

  def _clear_layout(self, layout):
    while layout.count():
      child = layout.takeAt(0)
      if child.widget():
        child.widget().deleteLater()
      elif child.layout():
        self._clear_layout(child.layout())