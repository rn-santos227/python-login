import modules.logs.controller as logs_controller

from PyQt5.QtGui import QColor
from PyQt5.QtWidgets import QDialog, QFrame, QGraphicsDropShadowEffect, QGridLayout, QHeaderView, QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from components.button import Button
from components.date_field import DateField
from components.message_dialog import MessageDialog
from components.prompt_dialog import PromptDialog

from modules.logs.model import StudentLog

from assets.styles.styles import content_frame_style

class LogsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.setStyleSheet(content_frame_style)
    self.pages_handler = pages_handler
    self.message_dialog: MessageDialog = MessageDialog(self)
    self.logs: list[StudentLog] = []
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
    search_layout: QGridLayout = QGridLayout()
    search_button_layout: QHBoxLayout = QHBoxLayout()
    field_layout: QHBoxLayout = QHBoxLayout()

    self.start_date: DateField = DateField("Start Date")
    self.end_date: DateField = DateField("End Date")

    field_layout.addWidget(self.start_date)
    field_layout.addWidget(self.end_date)

    search_button: Button = Button("Search Logs")
    search_button.connect_signal(self.search_logs)
    
    search_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    search_button_layout.addWidget(search_button)

    search_layout.addLayout(field_layout, 0, 0, 1, 2)
    search_layout.addLayout(search_button_layout, 1, 0, 1, 2)

    self.top_layout.addLayout(search_layout)
    self.top_layout.setContentsMargins(150, 0, 150, 20)

    self.table_widget: QTableWidget = QTableWidget()
    self.table_widget.setColumnCount(5)
    self.table_widget.setHorizontalHeaderLabels(["Student Name", "Date", "Time Login", "Time Logout", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.table_widget.verticalHeader().setVisible(False)

    content_layout.addLayout(self.top_layout)
    content_layout.addWidget(self.table_widget)
    content_layout.setContentsMargins(50, 20, 50, 20)

    self.main_layout.addWidget(content_frame)

    self.setLayout(self.main_layout)
    self.load_logs()

  def load_logs(self):
    self.logs = logs_controller.get_logs_with_students("LIMIT:100,DESC")
    self.table_widget.setRowCount(0)

    if not self.logs:
      return
    
    for log in self.logs:
      row_position = self.table_widget.rowCount()
      self.table_widget.insertRow(row_position)

      self.table_widget.setItem(row_position, 0, QTableWidgetItem(str(log.full_name)))
      self.table_widget.setItem(row_position, 1, QTableWidgetItem(str(log.date)))
      self.table_widget.setItem(row_position, 2, QTableWidgetItem(str(log.login_time)))
      self.table_widget.setItem(row_position, 3, QTableWidgetItem(str(log.logout_time)))

      user_type = self.pages_handler.session_handler.get_user_type()
      
      delete_button: QPushButton = QPushButton("Delete")
      delete_button.clicked.connect(lambda ch, log_id=log.log_id: self.__prompt_delete_log(log_id))

      button_layout: QHBoxLayout = QHBoxLayout()
      button_layout.addWidget(delete_button)
      button_layout.setContentsMargins(0, 0, 0, 0)

      button_widget: QWidget = QWidget()
      button_widget.setLayout(button_layout)

      self.table_widget.setCellWidget(row_position, 4, button_widget)

  def search_logs(self):
    start_date = self.start_date.get_date()
    end_date = self.end_date.get_date()

    self.logs = logs_controller.get_logs_with_students(f"date >= '{start_date}' AND date <= '{end_date}'")
    self.table_widget.setRowCount(0)

    if not self.logs:
      return
    
    for log in self.logs:
      row_position = self.table_widget.rowCount()
      self.table_widget.insertRow(row_position)

      self.table_widget.setItem(row_position, 0, QTableWidgetItem(str(log.full_name)))
      self.table_widget.setItem(row_position, 1, QTableWidgetItem(str(log.date)))
      self.table_widget.setItem(row_position, 2, QTableWidgetItem(str(log.login_time)))
      self.table_widget.setItem(row_position, 3, QTableWidgetItem(str(log.logout_time)))

      user_type = self.pages_handler.session_handler.get_user_type()
      
      if user_type is "admin":
        delete_button: QPushButton = QPushButton("Delete")
        delete_button.clicked.connect(lambda ch, log_id=log.log_id: self.__prompt_delete_log(log_id))

        button_layout: QHBoxLayout = QHBoxLayout()
        button_layout.addWidget(delete_button)
        button_layout.setContentsMargins(0, 0, 0, 0)

        button_widget: QWidget = QWidget()
        button_widget.setLayout(button_layout)

        self.table_widget.setCellWidget(row_position, 4, button_widget)

  def delete_log(self, log_id):
    logs_controller.delete_log(id=log_id)
    self.load_logs()
    self.message_dialog.show_message("Success", "Log has been deleted successfully.", "Information")

  def __prompt_delete_log(self, log_id):
    self.log_id = log_id
    prompt_dialog: PromptDialog = PromptDialog(title="Security Prompt", message="Enter your Admin Password", is_password=True)
    
    if prompt_dialog.exec_() == QDialog.Accepted:
      password = prompt_dialog.get_user_input()

      if self.pages_handler.session_handler.verify_password(password):
        self.delete_log(self.log_id)
      
      else:
        self.message_dialog.show_message("Information", "Password does not match.", "information")
