from PyQt5.QtWidgets import QPushButton, QSizePolicy, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont, QIcon, QPixmap, QPainter
from PyQt5.QtSvg import QSvgRenderer
from PyQt5.QtCore import QSize, Qt

from assets.styles.styles import button_style, button_icon_style

from handlers.asset_handler import AssetHandler

class Button(QWidget):
  def __init__(self, button_text="Button", parent=None):
    super().__init__(parent)
    self.__init_ui(button_text)

  def __init_ui(self, button_text):
    self.layout: QVBoxLayout = QVBoxLayout()
    self.button: QPushButton = QPushButton(button_text)
    self.button.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)

    button_font: QFont = QFont()
    button_font.setPointSize(12)
    self.button.setFont(button_font)

    self.button.setStyleSheet(button_style)

    self.layout.addWidget(self.button)
    self.setLayout(self.layout)

  def set_button_text(self, text):
    self.button.setText(text)

  def connect_signal(self, slot):
    self.button.clicked.connect(slot)

  def disconnect_signal(self, slot):
    self.button.clicked.disconnect(slot)

  def set_fixed_width(self, width):
    self.button.setFixedWidth(width)

  def set_font_size(self, size):
    button_font = self.button.font()
    button_font.setPointSize(size)
    self.button.setFont(button_font)

  def set_color(self, bg_color, font_color):
    self.button.setStyleSheet(f"background-color: {bg_color}; color: {font_color}")

  def set_enabled(self):
    self.button.setEnabled(True)

  def set_disabled(self):
    self.button.setEnabled(False)

  def set_svg_icon(self, sv_folder, svg_name, icon_size=16):
    asset_handler: AssetHandler = AssetHandler()
    svg_renderer: QSvgRenderer = asset_handler.get_svg(svg_folder=sv_folder, svg_name=svg_name)
    
    pixmap = QPixmap(icon_size, icon_size)
    pixmap.fill(Qt.transparent)
    painter = QPainter(pixmap)
    
    svg_renderer.render(painter)
    painter.end()
    
    icon = QIcon(pixmap)
    self.button.setIcon(icon)
    self.button.setIconSize(QSize(icon_size, icon_size))

    self.button.setStyleSheet(button_icon_style)

