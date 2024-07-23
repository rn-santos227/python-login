import modules.admin.controller as admin_controller

from PyQt5.QtWidgets import QDialog, QGridLayout, QHeaderView, QHBoxLayout, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from components.button import Button
from components.message_box import MessageBox
from components.question_box import QuestionBox
from components.text_field import TextField

from handlers.validations_handler import ValidationHandler

from modules.admin.model import Admin

class AdminsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.message_box = MessageBox(self)
    self.validation_handler = ValidationHandler()
    self.admins = []
    self.init_ui()

  def init_ui(self):
    self.main_layout: QVBoxLayout = QVBoxLayout()
    self.top_layout: QHBoxLayout = QHBoxLayout()
    
    self.top_layout.addLayout(self.init_create_layout())

    self.table_widget = QTableWidget()
    self.table_widget.setColumnCount(4)
    self.table_widget.setHorizontalHeaderLabels(["ID", "Full Name", "Email", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.table_widget.verticalHeader().setVisible(False)

    self.main_layout.addLayout(self.top_layout)
    self.main_layout.addWidget(self.table_widget)
  
    self.setLayout(self.main_layout)
    self.load_admins()

  def init_create_layout(self):
    create_layout = QGridLayout()
    self.create_button_layout = QHBoxLayout()

    self.email_field = TextField(label_text="Email", placeholder_text="Enter admin email.")
    self.password_field = TextField(label_text="Password", placeholder_text="Enter admin password.")
    self.password_field.text_field.setEchoMode(QLineEdit.Password)
    self.fullname_field = TextField(label_text="Full Name", placeholder_text="Enter admin full name.")

    create_button = Button("Create Admin")
    create_button.connect_signal(self.create_admin)

    self.create_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    self.create_button_layout.addWidget(create_button)

    create_layout.addWidget(self.email_field, 0, 0, 1, 2)
    create_layout.addWidget(self.password_field, 1, 0, 1, 2)
    create_layout.addWidget(self.fullname_field, 2, 0, 1, 2)
    create_layout.addLayout(self.create_button_layout, 3, 0, 1, 2)

    return create_layout

  def init_update_layout(self):
    update_layout = QGridLayout()
    self.update_button_layout = QHBoxLayout()

    self.update_email_field = TextField(label_text="Email", placeholder_text="Enter admin email.")
    self.update_password_field = TextField(label_text="Password", placeholder_text="Enter admin password.")
    self.update_password_field.text_field.setEchoMode(QLineEdit.Password)
    self.update_fullname_field = TextField(label_text="Full Name", placeholder_text="Enter admin full name.")

    update_button = Button("Update Student")
    update_button.connect_signal(self.update_admin)

    cancel_button = Button("Cancel Update")
    cancel_button.connect_signal(self.__switch_to_create_layout)

    self.update_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    self.update_button_layout.addWidget(update_button)
    self.update_button_layout.addWidget(cancel_button)
    
    update_layout.addWidget(self.update_email_field, 0, 0, 1, 2)
    update_layout.addWidget(self.update_password_field, 1, 0, 1, 2)
    update_layout.addWidget(self.update_fullname_field, 2, 0, 1, 2)
    update_layout.addLayout(self.update_button_layout, 3, 0, 1, 2)

    return update_layout

  def create_admin(self):
    email = self.email_field.get_text()
    password = self.password_field.get_text()
    full_name = self.fullname_field.get_text()

    fields_to_validate = [
      (self.validation_handler.is_valid_email, email, "Invalid email address."),
      (self.validation_handler.is_not_empty, password, "Password cannot be empty."),
      (self.validation_handler.is_not_empty, full_name, "Full name cannot be empty."),
    ]

    if not self.validation_handler.validate_fields(self, fields_to_validate):
      return
    
    new_admin = Admin(
      email = email,
      password = password,
      full_name = full_name,
      status = "active"
    )

    admin_controller.create_admin(new_admin)
    self.load_admins()
    self.__clear_fields()
    self.message_box.show_message("Success", "Admin has been created successfully.", "Information")
  
  def update_admin(self):
    email = self.update_email_field.get_text()
    password = self.update_password_field.get_text()
    full_name = self.update_fullname_field.get_text()

    fields_to_validate = [
      (self.validation_handler.is_valid_email, email, "Invalid email address."),
      (self.validation_handler.is_not_empty, password, "Password cannot be empty."),
      (self.validation_handler.is_not_empty, full_name, "Full name cannot be empty."),
    ]

    if not self.validation_handler.validate_fields(self, fields_to_validate):
      return
    
    update_admin = Admin(
      email = email,
      password = password,
      full_name = full_name
    )

    admin_controller.update_admin(update_admin)
    self.load_admins()
    self.__switch_to_create_layout()
    self.message_box.show_message("Success", "Admin has been updated successfully.", "Information")

  def delete_admin(self, admin_id):
    admin_controller.delete_admin(id=admin_id)
    self.load_admins()
    self.message_box.show_message("Success", "Admin has been deleted successfully.", "Information")

  def load_admins(self):
    self.admins = admin_controller.get_admins("status = 'active'", "select")
    self.table_widget.setRowCount(0)

    if not self.admins:
      return
      
    for admin in self.admins:
      row_position = self.table_widget.rowCount()
      self.table_widget.insertRow(row_position)

      self.table_widget.setItem(row_position, 0, QTableWidgetItem(str(admin.id)))
      self.table_widget.setItem(row_position, 1, QTableWidgetItem(admin.full_name))
      self.table_widget.setItem(row_position, 2, QTableWidgetItem(admin.email))

      update_button = QPushButton("Update")
      update_button.clicked.connect(lambda ch, admin=admin: self.__load_admin_for_update(admin))

      delete_button = QPushButton("Delete")
      delete_button.clicked.connect(lambda ch, admin_id=admin.id: self.__prompt_delete_admin(admin_id))

      button_layout = QHBoxLayout()
      button_layout.addWidget(update_button)
      button_layout.addWidget(delete_button)
      button_layout.setContentsMargins(0, 0, 0, 0)
      
      button_widget = QWidget()
      button_widget.setLayout(button_layout)
      
      self.table_widget.setCellWidget(row_position, 3, button_widget)

  def __prompt_delete_admin(self, admin_id: int):
    self.admin_id = admin_id
    question_box = QuestionBox(message="Do you want to delete this admin?")
    if question_box.exec() == QDialog.Accepted:
      self.delete_admin(admin_id=self.admin_id)

  def __load_admin_for_update(self, admin: Admin):
    self.__switch_to_update_layout()
    self.admin_id = admin.id

    self.update_email_field.set_text(admin.email)
    self.update_fullname_field.set_text(admin.full_name)

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
    self.email_field.clear_text()
    self.password_field.clear_text()
    self.fullname_field.clear_text()

  def __clear_layout(self, layout):
    while layout.count():
      child = layout.takeAt(0)
      if child.widget():
        child.widget().deleteLater()
      elif child.layout():
        self.__clear_layout(child.layout())