import modules.admin.controller as admin_controller

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog, QFrame, QGraphicsDropShadowEffect, QGridLayout, QHeaderView, QHBoxLayout, QLayout, QLayoutItem, QLineEdit, QPushButton, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from components.button import Button
from components.message_dialog import MessageDialog
from components.prompt_dialog import PromptDialog
from components.text_field import TextField

from handlers.validations_handler import ValidationHandler

from modules.admin.model import Admin

from assets.styles.styles import content_frame_style

class AdminsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.setStyleSheet(content_frame_style)
    self.pages_handler = pages_handler
    self.message_dialog: MessageDialog = MessageDialog(self)
    self.validation_handler: ValidationHandler = ValidationHandler()
    self.admins: list[Admin] = []
    self.__init_ui()

  def __init_ui(self):
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
    self.top_layout.setContentsMargins(150, 0, 150, 20)

    self.table_widget: QTableWidget = QTableWidget()
    self.table_widget.setColumnCount(4)
    self.table_widget.setHorizontalHeaderLabels(["ID", "Full Name", "Email", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Fixed)
    self.table_widget.setColumnWidth(0, 50)
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.table_widget.verticalHeader().setVisible(False)

    content_layout.addLayout(self.top_layout)
    content_layout.addWidget(self.table_widget)
    content_layout.setContentsMargins(50, 20, 50, 20)

    self.main_layout.addWidget(content_frame)
  
    self.setLayout(self.main_layout)
    self.load_admins()

  def init_create_layout(self):
    create_layout: QGridLayout = QGridLayout()
    self.create_button_layout: QHBoxLayout = QHBoxLayout()

    self.email_field: TextField = TextField(label_text="Email", placeholder_text="Enter admin email.")
    self.password_field: TextField = TextField(label_text="Password", placeholder_text="Enter admin password.")
    self.password_field.text_field.setEchoMode(QLineEdit.Password)
    self.fullname_field: TextField = TextField(label_text="Full Name", placeholder_text="Enter admin full name.")

    create_button: Button = Button("Create Admin")
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

    self.update_email_field: TextField = TextField(label_text="Email", placeholder_text="Enter admin email.")
    self.update_password_field: TextField = TextField(label_text="Password", placeholder_text="Enter admin password.")
    self.update_password_field.text_field.setEchoMode(QLineEdit.Password)
    self.update_fullname_field: TextField = TextField(label_text="Full Name", placeholder_text="Enter admin full name.")

    update_button: Button = Button("Update Student")
    update_button.connect_signal(self.update_admin)

    cancel_button: Button = Button("Cancel Update")
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
      (self.validation_handler.is_unique_admin_email, email, "Email has been taken."),
      (self.validation_handler.is_not_empty, password, "Password cannot be empty."),
      (self.validation_handler.is_not_empty, full_name, "Full name cannot be empty."),
    ]

    if not self.validation_handler.validate_fields(self, fields_to_validate):
      return
    
    new_admin: Admin = Admin(
      email = email,
      password = password,
      full_name = full_name,
      status = "active"
    )

    admin_controller.create_admin(new_admin)
    self.load_admins()
    self.__clear_fields()
    self.message_dialog.show_message("Success", "Admin has been created successfully.", "Information")
  
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
    
    update_admin: Admin = Admin(
      id = self.admin_id,
      email = email,
      password = password,
      full_name = full_name
    )

    admin_controller.update_admin(update_admin)
    self.load_admins()
    self.__switch_to_create_layout()
    self.message_dialog.show_message("Success", "Admin has been updated successfully.", "Information")

  def delete_admin(self, admin_id):
    admin_controller.delete_admin(id=admin_id)
    self.load_admins()
    self.message_dialog.show_message("Success", "Admin has been deleted successfully.", "Information")

  def load_admins(self):
    current_admin = self.pages_handler.session_handler.user
    
    if current_admin:
      query = f"status = 'active' AND id != {current_admin.id}"
    else:
      query = "status = 'active'"

    self.admins = admin_controller.get_admins(query, "select")
    self.table_widget.setRowCount(0)

    if not self.admins:
      return
      
    for admin in self.admins:
      row_position = self.table_widget.rowCount()
      self.table_widget.insertRow(row_position)

      self.table_widget.setItem(row_position, 0, QTableWidgetItem(str(admin.id)))
      self.table_widget.setItem(row_position, 1, QTableWidgetItem(admin.full_name))
      self.table_widget.setItem(row_position, 2, QTableWidgetItem(admin.email))

      update_button: QPushButton = QPushButton("Update")
      update_button.clicked.connect(lambda ch, admin=admin: self.__load_admin_for_update(admin))

      delete_button : QPushButton = QPushButton("Delete")
      delete_button.clicked.connect(lambda ch, admin_id=admin.id: self.__prompt_delete_admin(admin_id))

      button_layout: QHBoxLayout = QHBoxLayout()
      button_layout.addWidget(update_button)
      button_layout.addWidget(delete_button)
      button_layout.setContentsMargins(0, 0, 0, 0)
      
      button_widget: QWidget = QWidget()
      button_widget.setLayout(button_layout)
      
      self.table_widget.setCellWidget(row_position, 3, button_widget)

  def __prompt_delete_admin(self, admin_id: int):
    self.admin_id = admin_id
    prompt_dialog: PromptDialog = PromptDialog(title="Security Prompt", message="Enter your Admin Password", is_password=True)

    if prompt_dialog.exec_() == QDialog.Accepted:
      password = prompt_dialog.get_user_input()

      if self.pages_handler.session_handler.verify_password(password):
        self.delete_admin(self.admin_id)

      else:
        self.message_dialog.show_message("Information", "Password does not match.", "information")

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

  def __clear_layout(self, layout: QLayout):
    while layout.count():
      child: QLayoutItem = layout.takeAt(0)
      if child.widget():
        child.widget().deleteLater()
      elif child.layout():
        self.__clear_layout(child.layout())