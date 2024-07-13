import modules.logs.controller as logs_controller

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QGridLayout, QTableWidget, QTableWidgetItem, QHeaderView, QSpacerItem, QSizePolicy

from components.button import Button
from components.date_field import DateField

from modules.logs.handler import logs, update_logs

class LogsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.init_ui()

  def init_ui(self):
    self.main_layout = QVBoxLayout()
    self.top_layout = QHBoxLayout()
    search_layout = QGridLayout()
    search_button_layout = QHBoxLayout()
    field_layout = QHBoxLayout()

    self.start_date = DateField("Start Date")
    self.end_date = DateField("End Date")

    field_layout.addWidget(self.start_date)
    field_layout.addWidget(self.end_date)

    search_button = Button("Search Logs")
    
    search_button_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
    search_button_layout.addWidget(search_button)

    search_layout.addLayout(field_layout, 0, 0, 1, 2)
    search_layout.addLayout(search_button_layout, 1, 0, 1, 2)

    self.top_layout.addLayout(search_layout)

    self.table_widget = QTableWidget()
    self.table_widget.setColumnCount(5)
    self.table_widget.setHorizontalHeaderLabels(["Student Name", "Date", "Time Login", "Time Logout", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    self.main_layout.addLayout(self.top_layout)
    self.main_layout.addWidget(self.table_widget)

    self.setLayout(self.main_layout)
    self.load_logs()

  def load_logs(self):
    start_date = self.start_date.get_date()
    end_date = self.end_date.get_date()

    update_logs(start_date, end_date)
    self.table_widget.setRowCount(0)

    if not logs:
      return
    
    for log in logs:
      row_position = self.table_widget.rowCount()
      self.table_widget.insertRow(row_position)