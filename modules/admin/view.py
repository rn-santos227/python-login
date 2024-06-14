import modules.admin.controller as admin_controller

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QGridLayout,  QSpacerItem, QSizePolicy

from components.button import Button
from components.message_box import MessageBox
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
    self.main_layout = QVBoxLayout()
    self.top_layout = QHBoxLayout()
    
    self.top_layout.addLayout(self.init_create_layout())

    self.table_widget = QTableWidget()
    self.table_widget.setColumnCount(4)
    self.table_widget.setHorizontalHeaderLabels(["ID", "Full Name", "Email", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

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

    cancel_button = Button("Cancel Update")

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
  
  def load_admins(self):
    self.admins = admin_controller.get_admins("status = 'active'", "select")
    self.table_widget.setRowCount(0)

    if not self.admins:
      email = self.email_field.get_text()
      password = self.password_field.get_text()
      full_name = self.fullname_field.get_text()

      fields_to_validate = [
        (self.validation_handler.is_valid_email, email, "Invalid email address."),
        (self.validation_handler.is_not_empty, password, "Password cannot be empty."),
        (self.validation_handler.is_not_empty, full_name, "Full name cannot be empty.")
      ]
      
      if not self.validation_handler.validate_fields(self, fields_to_validate):
        return

      new_admin = Admin(
        full_name = full_name,
        email = email,
        password = password,
        status = "active"
      )

      admin_controller.create_admin(new_admin)
      self.load_admins()
      self._clear_fields()
      self.message_box.show_message("Success", "Admin has been created successfully.", "Information")
      
    for admin in self.admins:
      row_position = self.table_widget.rowCount()
      self.table_widget.insertRow(row_position)

      self.table_widget.setItem(row_position, 0, QTableWidgetItem(str(admin.id)))
      self.table_widget.setItem(row_position, 1, QTableWidgetItem(admin.full_name))
      self.table_widget.setItem(row_position, 2, QTableWidgetItem(admin.email))

      update_button = QPushButton("Update")
      delete_button = QPushButton("Delete")

      button_layout = QHBoxLayout()
      button_layout.addWidget(update_button)
      button_layout.addWidget(delete_button)
      button_layout.setContentsMargins(0, 0, 0, 0)
      
      button_widget = QWidget()
      button_widget.setLayout(button_layout)
      
      self.table_widget.setCellWidget(row_position, 3, button_widget)

  def _clear_fields(self):
    self.email_field.clear_text()
    self.password_field.clear_text()
    self.fullname_field.clear_text()