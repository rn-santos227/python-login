import modules.parents.controller as parent_controller
import modules.students.controller as student_controller

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QTableWidget, QHeaderView, QGridLayout, QSpacerItem, QSizePolicy, QTableWidgetItem, QPushButton

from components.button import Button
from components.combo_box import ComboBox
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
    self.load_parents()

  def init_create_layout(self):
    create_layout = QGridLayout()
    self.create_button_layout = QHBoxLayout()
    
    self.student_combo_box = ComboBox(label_text="Student Name", items=self.load_students_to_combo_box())
    self.parent_name_field = TextField(label_text="Parent Full Name", placeholder_text="Enter parent full name.")
    self.parent_contact_field = TextField(label_text="Contact Number", placeholder_text="Enter parent contact number.")

    create_button = Button("Create Parent")

    self.create_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    self.create_button_layout.addWidget(create_button)

    create_layout.addWidget(self.student_combo_box, 0, 0, 1, 2)
    create_layout.addWidget(self.parent_name_field, 1, 0, 1, 2)
    create_layout.addWidget(self.parent_contact_field, 2, 0, 1, 2)
    create_layout.addLayout(self.create_button_layout, 3, 0, 1, 2)

    return create_layout
  
  def init_update_layout(self):
    update_layout = QGridLayout()
    self.update_button_layout = QHBoxLayout()

    self.update_student_combo_box = ComboBox(label_text="Student Name", items=self.load_students_to_combo_box())
    self.update_parent_name_field = TextField(label_text="Parent Full Name", placeholder_text="Enter parent full name.")
    self.update_parent_contact_field = TextField(label_text="Contact Number", placeholder_text="Enter parent contact number.")

    update_button = Button("Update Parent")

    cancel_button = Button("Cancel Update")
  
    self.update_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    self.update_button_layout.addWidget(update_button)
    self.update_button_layout.addWidget(cancel_button)

    update_layout.addWidget(self.update_student_combo_box, 0, 0, 1, 2)
    update_layout.addWidget(self.update_parent_name_field, 1, 0, 1, 2)
    update_layout.addWidget(self.update_parent_contact_field, 2, 0, 1, 2)
    update_layout.addLayout(self.update_button_layout, 3, 0, 1, 2)

    return update_layout
  
  def load_students_to_combo_box(self):
    students = student_controller.get_students("status = 'active'", "select")
    if not students:
      return
    
    return [(student.full_name, student.id) for student in students]

  def load_parents(self):
    self.parents = parent_controller.get_parents("status = 'active'", "select")
    self.table_widget.setRowCount(0)

    if not self.parents:
      return
    
    for parent in self.parents:
      row_position = self.table_widget.rowCount()

      self.table_widget.setItem(row_position, 0, QTableWidgetItem(str(parent.id)))
      self.table_widget.setItem(row_position, 1, QTableWidgetItem(str(parent.student.full_name)))
      self.table_widget.setItem(row_position, 2, QTableWidgetItem(str(parent.full_name)))
      self.table_widget.setItem(row_position, 3, QTableWidgetItem(str(parent.contact)))

      update_button = QPushButton("Update")

      delete_button = QPushButton("Delete")

      button_layout = QHBoxLayout()

  def _clear_fields(self):
    self.parent_name_field.clear_text()
    self.parent_contact_field.clear_text()
    