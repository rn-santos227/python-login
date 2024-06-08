class PagesHandler:
  def __init__(self, stacked_widget, login_page, dasboard_page):
    self.stacked_widget = stacked_widget
    self.login_page = login_page
    self.dasboard_page = dasboard_page

  def switch_to_login_page(self):
    self.stacked_widget.setCurrentWidget(self.login_page)

  def switch_to_dashboard_page(self):
    self.stacked_widget.setCurrentWidget(self.dasboard_page)