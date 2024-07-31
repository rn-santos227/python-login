
from PyQt5.QtWidgets import QStackedWidget

from modules.auth.view import LoginPage
from modules.dashboard.view import DashboardAdminPage

class PagesHandler:
  def __init__(self, stacked_widget: QStackedWidget):
    self.stacked_widget: QStackedWidget = stacked_widget
    self.login_page: LoginPage = LoginPage(self)
    self.dashboard_page: LoginPage = DashboardAdminPage(self)

  def switch_to_login_page(self):
    self.stacked_widget.setCurrentWidget(self.login_page)

  def switch_to_dashboard_page(self):
    self.stacked_widget.setCurrentWidget(self.dashboard_page)