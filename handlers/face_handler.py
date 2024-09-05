import os

class FaceHandler:
  def __init__(self):
    self.faces_folder = os.path.join(os.environ["USERPROFILE"], "Documents", "Faces")