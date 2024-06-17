import modules.parents.controller as parent_controller
import modules.students.controller as student_controller

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QHeaderView, QGridLayout,  QSpacerItem, QSizePolicy

from components.button import Button
from components.message_box import MessageBox
from components.text_field import TextField

from handlers.validations_handler import ValidationHandler
from modules.parents.model import Parent

class ParentsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.message_box = MessageBox(self)
    self.validation_handler = ValidationHandler()
    self.parents = []
    self.students = []
    self.init_ui()

  def init_ui(self):
    self.main_layout = QVBoxLayout()
    self.top_layout = QHBoxLayout()

    self.top_layout.addLayout(self.init_create_layout())

    self.table_widget = QTableWidget()
    self.table_widget.setColumnCount(5)
    self.table_widget.setHorizontalHeaderLabels(["ID", "Student Name", "Parent Name", "Contact Number", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    self.main_layout.addLayout(self.top_layout)
    self.main_layout.addWidget(self.table_widget)
  
    self.setLayout(self.main_layout)

  def init_create_layout(self):
    create_layout = QGridLayout()
    self.create_button_layout = QHBoxLayout()

    self.student_name_field = TextField(label_text="Student Name", placeholder_text="Enter student name.")
    self.parent_name_field = TextField(label_text="Parent Full Name", placeholder_text="Enter parent full name.")
    self.parent_contact_field = TextField(label_text="Contact Number", placeholder_text="Enter parent contact number.")

    create_button = Button("Create Parent")

    self.create_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    self.create_button_layout.addWidget(create_button)

    create_layout.addWidget(self.student_name_field, 0, 0, 1, 2)
    create_layout.addWidget(self.parent_name_field, 1, 0, 1, 2)
    create_layout.addWidget(self.parent_contact_field, 2, 0, 1, 2)
    create_layout.addLayout(self.create_button_layout, 3, 0, 1, 2)

    return create_layout
  
  def load_students_to_dropdown(self):
    pass

  def _clear_fields(self):
    self.student_name_field.clear_text()
    self.parent_name_field.clear_text()
    self.parent_contact_field.clear_text()
    