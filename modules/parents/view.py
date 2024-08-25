import modules.parents.controller as parents_controller
import modules.students.controller as students_controller

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog, QFrame, QGraphicsDropShadowEffect, QGridLayout, QHeaderView, QHBoxLayout, QLayout, QLayoutItem, QPushButton, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from components.button import Button
from components.combo_box import ComboBox
from components.message_box import MessageBox
from components.question_box import QuestionBox
from components.text_field import TextField

from handlers.validations_handler import ValidationHandler
from modules.parents.model import Parent

from assets.styles.styles import content_frame_style

class ParentsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.setStyleSheet(content_frame_style)
    self.pages_handler = pages_handler
    self.message_box: MessageBox = MessageBox(self)
    self.validation_handler: ValidationHandler = ValidationHandler()
    self.students = []
    self.parents = []
    self.init_ui()

  def init_ui(self):
    content_frame: QFrame = QFrame(self)
    content_frame.setObjectName("contentFrame")
    content_layout: QVBoxLayout = QVBoxLayout(content_frame)

    shadow_effect: QGraphicsDropShadowEffect = QGraphicsDropShadowEffect()
    shadow_effect.setBlurRadius(15)
    shadow_effect.setColor(QColor(0, 0, 0, 160))
    shadow_effect.setOffset(0, 5)

    content_frame.setGraphicsEffect(shadow_effect)

    self.main_layout: QVBoxLayout = QVBoxLayout()
    self.top_layout: QHBoxLayout = QHBoxLayout()

    self.top_layout.addLayout(self.init_create_layout())

    self.table_widget: QTableWidget = QTableWidget()
    self.table_widget.setColumnCount(5)
    self.table_widget.setHorizontalHeaderLabels(["ID", "Student Name", "Parent Name", "Contact Number", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.table_widget.verticalHeader().setVisible(False)

    content_layout.addLayout(self.top_layout)
    content_layout.addWidget(self.table_widget)
    content_layout.setContentsMargins(50, 50, 50, 50)

    self.main_layout.addWidget(content_frame)
  
    self.setLayout(self.main_layout)
    self.load_parents()

  def init_create_layout(self):
    create_layout: QGridLayout = QGridLayout()
    self.create_button_layout: QHBoxLayout = QHBoxLayout()
    
    self.student_combo_box: ComboBox = ComboBox(label_text="Student Name")
    self.load_students_to_combo_box()

    self.parent_name_field: TextField = TextField(label_text="Parent Full Name", placeholder_text="Enter parent full name.")
    self.parent_contact_field: TextField = TextField(label_text="Contact Number", placeholder_text="Enter parent contact number.")

    create_button: Button = Button("Create Parent")
    create_button.connect_signal(self.create_parent)

    self.create_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    self.create_button_layout.addWidget(create_button)

    create_layout.addWidget(self.student_combo_box, 0, 0, 1, 2)
    create_layout.addWidget(self.parent_name_field, 1, 0, 1, 2)
    create_layout.addWidget(self.parent_contact_field, 2, 0, 1, 2)
    create_layout.addLayout(self.create_button_layout, 3, 0, 1, 2)

    return create_layout
  
  def init_update_layout(self):
    update_layout: QGridLayout = QGridLayout()
    self.update_button_layout: QHBoxLayout = QHBoxLayout()

    self.update_student_combo_box: ComboBox = ComboBox(label_text="Student Name")
    self.load_students_to_combo_box()
    
    self.update_parent_name_field: TextField = TextField(label_text="Parent Full Name", placeholder_text="Enter parent full name.")
    self.update_parent_contact_field: TextField = TextField(label_text="Contact Number", placeholder_text="Enter parent contact number.")

    update_button: Button = Button("Update Parent")
    update_button.connect_signal(self.update_parent)

    cancel_button: Button = Button("Cancel Update")
    cancel_button.connect_signal(self.__switch_to_create_layout)
  
    self.update_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    self.update_button_layout.addWidget(update_button)
    self.update_button_layout.addWidget(cancel_button)

    update_layout.addWidget(self.update_student_combo_box, 0, 0, 1, 2)
    update_layout.addWidget(self.update_parent_name_field, 1, 0, 1, 2)
    update_layout.addWidget(self.update_parent_contact_field, 2, 0, 1, 2)
    update_layout.addLayout(self.update_button_layout, 3, 0, 1, 2)

    return update_layout
  
  def load_students_to_combo_box(self, update=False):
    self.students = students_controller.get_students("status = 'active'", "select")

    if not self.students:
      return
    
    items = [(student.full_name, student.id) for student in self.students]

    if update:
      self.update_student_combo_box.set_items(items)
    
    else:
      self.student_combo_box.set_items(items)
  
  def load_parents(self):
    self.parents = parents_controller.get_parents("all", "select")
    self.table_widget.setRowCount(0)

    if not self.parents:
      return
    
    for parent in self.parents:
      row_position = self.table_widget.rowCount()
      self.table_widget.insertRow(row_position)
      
      self.table_widget.setItem(row_position, 0, QTableWidgetItem(str(parent.id)))
      self.table_widget.setItem(row_position, 1, QTableWidgetItem(str(parent.student.full_name)))
      self.table_widget.setItem(row_position, 2, QTableWidgetItem(str(parent.full_name)))
      self.table_widget.setItem(row_position, 3, QTableWidgetItem(str(parent.email)))
      self.table_widget.setItem(row_position, 4, QTableWidgetItem(str(parent.contact)))

      update_button: QPushButton = QPushButton("Update")
      update_button.clicked.connect(lambda ch, parent=parent: self.__load_parent_for_update(parent))

      delete_button: QPushButton = QPushButton("Delete")
      delete_button.clicked.connect(lambda ch, parent_id=parent.id: self.__prompt_delete_parent(parent_id))

      button_layout: QHBoxLayout = QHBoxLayout()
      button_layout.addWidget(update_button)
      button_layout.addWidget(delete_button)
      button_layout.setContentsMargins(0, 0, 0, 0)

      button_widget: QWidget = QWidget()
      button_widget.setLayout(button_layout)

      self.table_widget.setCellWidget(row_position, 5, button_widget)

  def create_parent(self):
    student_id = self.student_combo_box.get_selected_value()
    parent_name = self.parent_name_field.get_text()
    contact = self.parent_contact_field.get_text()

    fields_to_validate = [
      (self.validation_handler.is_not_empty, student_id, "Student cannot be empty."),
      (self.validation_handler.is_not_empty, parent_name, "Parent's full name cannot be empty."),
      (self.validation_handler.is_not_empty, contact, "Contacts cannot be empty."),
    ]

    if not self.validation_handler.validate_fields(self, fields_to_validate):
      return

    new_parent: Parent = Parent(
      student_id = student_id,
      full_name = parent_name,
      contact = contact,
    )

    parents_controller.create_parent(new_parent)
    self.load_parents()
    self.__clear_fields()
    self.message_box.show_message("Success", "Parent has been created successfully.", "Information")

  def update_parent(self):
    student_id = self.update_student_combo_box.get_selected_value()
    parent_name = self.update_parent_name_field.get_text()
    contact = self.update_parent_contact_field.get_text()

    fields_to_validate = [
      (self.validation_handler.is_not_empty, student_id, "Student cannot be empty."),
      (self.validation_handler.is_not_empty, parent_name, "Parent's full name cannot be empty."),
      (self.validation_handler.is_not_empty, contact, "Contacts cannot be empty."),
    ]

    if not self.validation_handler.validate_fields(self, fields_to_validate):
      return
    
    update_parent: Parent = Parent(
      id = self.parent_id,
      student_id = student_id,
      full_name = parent_name,
      contact = contact
    )

    parents_controller.update_parent(update_parent)
    self.load_parents()
    self.__switch_to_create_layout()
    self.message_box.show_message("Success", "Parent has been updated successfully.", "Information")

  def delete_parent(self, parent_id):
    parents_controller.delete_parent(parent_id)
    self.load_parents()
    self.message_box.show_message("Success", "Parent has been deleted successfully.", "Information")

  def __prompt_delete_parent(self, parent_id: int):
    self.parent_id = parent_id
    question_box: QuestionBox = QuestionBox(message="Do you want to delete this parent record?")
    if question_box.exec() == QDialog.Accepted:
      self.delete_parent(parent_id=self.parent_id)

  def __load_parent_for_update(self, parent: Parent):
    self.__switch_to_update_layout()
    self.parent_id = parent.id

    self.update_student_combo_box.set_selected_value(parent.student_id)
    self.update_parent_name_field.set_text(parent.full_name)
    self.update_parent_contact_field.set_text(parent.contact)

  def __switch_to_update_layout(self):
    while self.top_layout.count():
      child = self.top_layout.takeAt(0)
      if child.widget():
        child.widget().deleteLater()
      elif child.layout():
        self.__clear_layout(child.layout())
    self.top_layout.addLayout(self.init_update_layout())

  def __switch_to_create_layout(self):
    while self.top_layout.count():
      child = self.top_layout.takeAt(0)
      if child.widget():
        child.widget().deleteLater()
      elif child.layout():
        self.__clear_layout(child.layout())
    self.top_layout.addLayout(self.init_create_layout())
    self.__clear_fields()

  def __clear_fields(self):
    self.parent_name_field.clear_text()
    self.parent_contact_field.clear_text()

  def __clear_layout(self, layout: QLayout):
    while layout.count():
      child: QLayoutItem = layout.takeAt(0)
      if child.widget():
        child.widget().deleteLater()
      elif child.layout():
        self.__clear_layout(child.layout())
    