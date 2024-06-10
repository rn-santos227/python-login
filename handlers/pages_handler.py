
from modules.auth.view import LoginPage
from modules.dashboard.view import DashboardAdminPage

class PagesHandler:
  def __init__(self, stacked_widget):
    self.stacked_widget = stacked_widget
    self.login_page = LoginPage(self)
    self.dashboard_page = DashboardAdminPage(self)

  def switch_to_login_page(self):
    self.stacked_widget.setCurrentWidget(self.login_page)

  def switch_to_dashboard_page(self):
    self.stacked_widget.setCurrentWidget(self.dashboard_page)