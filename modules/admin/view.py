import modules.admin.controller as admin_controller

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox,  QSpacerItem, QSizePolicy

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
    main_layout = QHBoxLayout()
    left_layout = QHBoxLayout()
    button_layout = QHBoxLayout()

    create_layout = QVBoxLayout()

    self.email_field = TextField(label_text="Email", placeholder_text="Enter admin email.")
    self.password_field = TextField(label_text="Password", placeholder_text="Enter admin password.")
    self.password_field.text_field.setEchoMode(QLineEdit.Password)
    self.fullname_field = TextField(label_text="Full Name", placeholder_text="Enter admin full name.")

    create_button = Button("Create Admin")

    button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    button_layout.addWidget(create_button)

    create_layout.addWidget(self.email_field)
    create_layout.addWidget(self.password_field)
    create_layout.addWidget(self.fullname_field)
    create_layout.addLayout(button_layout)

    left_layout.addLayout(create_layout)

    self.table_widget = QTableWidget()
    self.table_widget.setColumnCount(4)
    self.table_widget.setHorizontalHeaderLabels(["ID", "Full Name", "Email", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    main_layout.addLayout(left_layout)
    main_layout.addWidget(self.table_widget)
  
    self.setLayout(main_layout)
    self.load_admins()

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
      delete_button = QPushButton("Delete")

      button_layout = QHBoxLayout()
      button_layout.addWidget(update_button)
      button_layout.addWidget(delete_button)
      button_layout.setContentsMargins(0, 0, 0, 0)
      
      button_widget = QWidget()
      button_widget.setLayout(button_layout)
      
      self.table_widget.setCellWidget(row_position, 3, button_widget)