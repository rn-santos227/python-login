import modules.logs.controller as logs_controller

from PyQt5.QtWidgets import QDialog, QGridLayout, QHeaderView, QHBoxLayout, QPushButton, QSizePolicy, QSpacerItem, QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget

from components.button import Button
from components.date_field import DateField
from components.message_box import MessageBox
from components.question_box import QuestionBox

class LogsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.message_box: MessageBox = MessageBox(self)
    self.logs = []
    self.init_ui()

  def init_ui(self):
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
    
    search_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    search_button_layout.addWidget(search_button)

    search_layout.addLayout(field_layout, 0, 0, 1, 2)
    search_layout.addLayout(search_button_layout, 1, 0, 1, 2)

    self.top_layout.addLayout(search_layout)

    self.table_widget: QTableWidget = QTableWidget()
    self.table_widget.setColumnCount(5)
    self.table_widget.setHorizontalHeaderLabels(["Student Name", "Date", "Time Login", "Time Logout", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    self.table_widget.verticalHeader().setVisible(False)

    self.main_layout.addLayout(self.top_layout)
    self.main_layout.addWidget(self.table_widget)

    self.setLayout(self.main_layout)
    self.load_logs()

  def load_logs(self):
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

      delete_button: QPushButton = QPushButton("Delete")
      delete_button.clicked.connect(lambda ch, log_id=log.log_id: self.__prompt_delete_log(log_id))

      button_layout: QHBoxLayout = QHBoxLayout()
      button_layout.addWidget(delete_button)
      button_layout.setContentsMargins(0, 0, 0, 0)

      button_widget: QWidget = QWidget()
      button_widget.setLayout(button_layout)

      self.table_widget.setCellWidget(row_position, 4, button_widget)

  def search_logs(self):
    pass

  def delete_log(self, log_id):
    logs_controller.delete_log(id=log_id)
    self.load_logs()
    self.message_box.show_message("Success", "Log has been deleted successfully.", "Information")

  def __prompt_delete_log(self, log_id):
    self.log_id = log_id
    question_box: QuestionBox = QuestionBox(message="Do you want to delete this log?")
    if question_box.exec() == QDialog.Accepted:
      self.delete_log(log_id=self.log_id)