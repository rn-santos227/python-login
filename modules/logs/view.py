import modules.logs.controller as logs_controller

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QGridLayout, QTableWidget, QTableWidgetItem, QHeaderView, QSpacerItem, QSizePolicy

from components.button import Button
from components.date_field import DateField

from modules.logs.handler import logs

class LogsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.init_ui()

  def init_ui(self):
    self.main_layout = QHBoxLayout()
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

    search_layout.addLayout(field_layout)
    search_layout.addLayout(search_button_layout)

    self.top_layout.addLayout(search_layout)

    self.table_widget = QTableWidget()
    self.table_widget.setColumnCount(5)
    self.table_widget.setHorizontalHeaderLabels(["Student Name", "Date", "Time Login", "Time Logout", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    self.main_layout.addLayout(self.top_layout)
    self.main_layout.addWidget(self.table_widget)
    self.setLayout(self.main_layout)

  def load_logs(self):
    pass