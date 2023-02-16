import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

class Paint(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("A simple paint program")
        self.setGeometry(100, 100, 640, 480) # set the window geometry

        # create a QPainter instance to draw on the widget
        self.painter = QPainter()
        self.image = QImage(self.size(), QImage.Format_ARGB32)
        self.image.fill(Qt.white) # fill the image with white color

    def paintEvent(self, event):
        # draw the image on the widget
        self.painter.begin(self)
        self.painter.drawImage(self.rect(), self.image, self.image.rect())
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

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Paint()
    window.show()
    sys.exit(app.exec())