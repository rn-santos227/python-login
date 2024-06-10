import modules.logs.controller as logs_controller

from PyQt5.QtWidgets import QWidget, QHBoxLayout, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QHeaderView, QMessageBox,  QSpacerItem, QSizePolicy

class LogsPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler
    self.logs = []
    self.init_ui()

  def init_ui(self):
    main_layout = QHBoxLayout()

    self.table_widget = QTableWidget()
    self.table_widget.setColumnCount(4)
    self.table_widget.setHorizontalHeaderLabels(["Student Name", "Time Login", "Time Logout", "Actions"])
    self.table_widget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    main_layout.addWidget(self.table_widget)
    self.setLayout(main_layout)
   