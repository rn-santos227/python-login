
from PyQt5.QtWidgets import QStackedWidget

from handlers.session_handler import SessionHandler

from modules.auth.view import LoginPage
from modules.dashboard.admins.view import DashboardAdminPage
from modules.dashboard.guards.view import DashboardGuardPage
from modules.dashboard.students.view import DashboardStudentPage

class PagesHandler:
  def __init__(self, stacked_widget: QStackedWidget):
    self.session_handler: SessionHandler = SessionHandler()
    self.stacked_widget: QStackedWidget = stacked_widget

    self.login_page: LoginPage = LoginPage(self, self.session_handler)
    self.dashboard_admin_page: DashboardAdminPage = DashboardAdminPage(self, self.session_handler)
    self.dashboard_guard_page: DashboardGuardPage = DashboardGuardPage(self, self.session_handler)
    self.dashboard_student_page: DashboardStudentPage = DashboardStudentPage(self, self.session_handler)

  def switch_to_login_page(self):
    self.stacked_widget.setCurrentWidget(self.login_page)

  def switch_to_dashboard_admin_page(self):
    self.stacked_widget.setCurrentWidget(self.dashboard_admin_page)
    self.dashboard_admin_page.logs_content.load_logs()

  def switch_to_dashboard_guard_page(self):
    self.stacked_widget.setCurrentWidget(self.dashboard_guard_page)
    self.dashboard_guard_page.logs_content.load_logs()

  def switch_to_dashboard_student_page(self):
    self.stacked_widget.setCurrentWidget(self.dashboard_student_page)
    self.dashboard_student_page.logs_content.load_logs()