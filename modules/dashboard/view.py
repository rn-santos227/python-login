from PyQt5.QtWidgets import QWidget

class DashboardPage(QWidget):
  def __init__(self, pages_handler):
    super().__init__()
    self.pages_handler = pages_handler