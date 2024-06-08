import modules.admin.controller as admin_controller

from modules.admin.model import Admin

def create_default_user():
  admin = Admin(full_name="Administrator", email="test@test.com", password="test@123", status="active")
  created_admin = admin_controller.create_admin(admin)
  print(created_admin)