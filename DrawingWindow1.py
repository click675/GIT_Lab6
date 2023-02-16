import sys
import random
from PySide6.QtCore import Qt, QTimer
from PySide6.QtGui import QPainter, QPen, QBrush, QColor
from PySide6.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QVBoxLayout

class Cookie(QWidget):
    def __init__(self):
        super().__init__()

        # set up the cookie appearance
        self.setFixedSize(100, 100)
        self.setStyleSheet('''
            background-color: #FFCC99;
            border: 1px solid black;
            border-radius: 50px;
        ''')
        self.setCursor(Qt.PointingHandCursor)

        # set up the cookie's counter
        self.clicks = 0
        self.label = QLabel(str(self.clicks), self)
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setGeometry(0, 0, 100, 100)

    def mousePressEvent(self, event):
        self.clicks += 1
        self.label.setText(str(self.clicks))
        self.parent().on_cookie_clicked()

class CookieClickerGame(QWidget):
    def __init__(self):
        super().__init__()

        # set up the layout
        layout = QVBoxLayout(self)
        layout.setSpacing(20)
        layout.setAlignment(Qt.AlignCenter)

        # set up the cookie
        self.cookie = Cookie()
        layout.addWidget(self.cookie)

        # set up the score display
        self.score = QLabel('Score: 0', self)
        self.score.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.score)

        # set up the timer for automatic cookie generation
        self.cookie_timer = QTimer()
        self.cookie_timer.timeout.connect(self.generate_cookie)
        self.cookie_timer.start(1000) # 1 cookie per second

    def generate_cookie(self):
        # add a new cookie to the layout at a random position
        x = self.width() * (0.1 + 0.8 * random.random())
        y = self.height() * (0.1 + 0.8 * random.random())
        cookie = Cookie()
        cookie.move(x, y)
        cookie.show()

    def on_cookie_clicked(self):
        self.cookie.clicks += 1
        self.cookie.label.setText(str(self.cookie.clicks))
        self.update_score()

    def update_score(self):
        self.score.setText('Score: ' + str(self.cookie.clicks))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    game = CookieClickerGame()
    game.show()
    sys.exit(app.exec_())