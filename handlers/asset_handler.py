import os
from PyQt5.QtGui import QPixmap

class AssetHandler:
  def __init__(self, assets_dir="assets"):
    self.assets_dir = assets_dir

  def get_image(self, image_name):
    image_path = os.path.join(self.assets_dir, image_name)