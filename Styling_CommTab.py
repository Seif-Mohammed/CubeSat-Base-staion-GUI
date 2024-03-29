
from PyQt6.QtGui import QPixmap,QPainter
from PyQt6.QtWidgets import  QWidget
from PyQt6.QtGui import QPixmap
from COMM_Tab import Ui_Form
import os


class Styling_CommTab(QWidget,Ui_Form):
    def __init__(self):
        super(Styling_CommTab, self).__init__()
        self.setupUi(self)
        # Set the size of the widget
        self.setGeometry(100, 100, 800, 600)

        background_file_path = os.path.join(os.path.dirname(__file__), "images", "background.jpg")

        # Load the background image
        self.background_image = QPixmap(background_file_path)

    def paintEvent(self, event):
        painter = QPainter(self)
        
        # Draw the background image
        painter.drawPixmap(self.rect(), self.background_image)