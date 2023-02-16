import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *

from ui_DrawingWidget import Ui_Form

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QWidget()
    form = Ui_Form()
    form.setupUi(window)
    form.pushButton.clicked.connect(form.widget.clear)
    window.show()
    sys.exit(app.exec())