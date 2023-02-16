import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Paint(QWidget):
     def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("A simple paint program")