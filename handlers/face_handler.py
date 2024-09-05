import os

class FaceHandler:
  def __init__(self):
    self.documents_folder = os.path.join(os.environ["USERPROFILE"], "Documents", "Faces")
    os.makedirs(self.documents_folder, exist_ok=True)

  def save_face(self, image_data, student_id):
    image_filename = f"{student_id}_face.png"