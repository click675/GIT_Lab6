import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *


class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.line = QPixmap("images/line.jpg")
        self.square = QPixmap("images/square.jpeg")
        self.time = 0
        self.timer = QTimer()
        self.timer.timeout.connect(self.paint)
        self.timer.start(10)

    def paint(self):
        self.time = (self.time + 1) % 50
        self.update()

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.drawPixmap(QRect(100, 200 + (-10 * self.time + 0.2 *
                     self.time ** 2), 100, 100), self.square)
        p.drawPixmap(QRect(100, 300, 200, 20), self.line)
        p.end()


def main():
    app = QApplication(sys.argv)
    w = Simple_drawing_window()
    w.show()

    return app.exec()


if __name__ == "__main__":
    sys.exit(main())
