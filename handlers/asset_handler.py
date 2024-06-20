import os
from PyQt5.QtGui import QPixmap

class AssetHandler:
  def __init__(self, assets_dir="assets"):
    self.assets_dir = assets_dir