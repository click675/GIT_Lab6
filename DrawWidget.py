import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class DrawWidget(QWidget):

    def __init__(self, parent = None):
        QWidget.__init__(self, parent)
        self.setWindowTitle("A simple paint program")
        self.setGeometry(100, 100, 640, 480)  # set the window geometry

        # create a QPainter instance to draw on the widget
        self.painter = QPainter(self)
        self.image = QImage(self.size(), QImage.Format_ARGB32)
        self.image.fill(Qt.white)  # fill the image with white color
        self.erase = False

    def paintEvent(self, event):
        # draw the image on the widget
        self.painter.begin(self)
        self.painter.drawImage(self.rect(), self.image, self.image.rect())
        # if self.erase:
        #     print("erase")
        #     # self.painter.end()
        #     # self.painter.begin(self.image)
        #     # self.painter.setBrush(QBrush(Qt.white, Qt.SolidPattern))
        #     # self.painter.drawRect(0, 0, 10000, 10000)
        #     self.image.fill(Qt.white)
        #     self.erase = False
        #     self.update()
        self.painter.end()

    def mousePressEvent(self, event):
        # start drawing when the mouse button is pressed
        if event.button() == Qt.LeftButton:
            self.last_point = event.pos()

    def mouseMoveEvent(self, event):
        # draw a line between the last point and the current point
        if event.buttons() and Qt.LeftButton:
            self.painter.begin(self.image)
            self.painter.setPen(QPen(Qt.black, 2, Qt.SolidLine))
            self.painter.drawLine(self.last_point, event.pos())
            self.painter.end()
            self.last_point = event.pos()
            self.update()
            self.image.resize
            print(self.image.rect())
            print(self.rect())

    def resizeEvent(self, e):
        self.image = self.image.scaled(self.width(), self.height())

    def clear(self):
        # print("clear")
        # self.erase = True
        self.image.fill(Qt.white)
        self.update()