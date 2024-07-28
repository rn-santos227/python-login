import os
from PyQt5.QtGui import QPixmap
from PyQt5.QtSvg import QSvgRenderer

class AssetHandler:
  def __init__(self, assets_dir="assets"):
    self.assets_dir = assets_dir

  def get_image(self, image_name):
    image_path = os.path.join(f"{self.assets_dir}/images", image_name)
    
    if os.path.exists(image_path):
      return QPixmap(image_path)
    
    else:
      raise FileNotFoundError(f"Image {image_name} not found in {self.assets_dir}")
    
  def get_svg(self, svg_name):
    svg_path = os.path.join(f"{self.assets_dir}/svg", svg_name)

    if os.path.exists(svg_path):
      svg_renderer = QSvgRenderer(svg_path)