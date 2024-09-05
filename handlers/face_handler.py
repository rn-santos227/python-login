import os
import cv2

class FaceHandler:
  def __init__(self):
    self.documents_folder = os.path.join(os.environ["USERPROFILE"], "Documents", "Faces")
    os.makedirs(self.documents_folder, exist_ok=True)

  def save_face(self, image_data, student_id) -> str:
    image_filename = f"{student_id}_face.png"
    image_path = os.path.join(self.documents_folder, image_filename)
    cv2.imwrite(image_path, image_data)

    return image_path