import os

class FaceHandler:
  def __init__(self):
    self.documents_folder = os.path.join(os.environ["USERPROFILE"], "Documents", "Faces")
    
    if not os.path.exists(self.documents_folder):
      os.makedirs(self.documents_folder)