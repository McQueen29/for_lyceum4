import sys
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5 import uic


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.do_paint = False
        self.btn_create.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        rx = randint(75, 450)
        yx = randint(75, 450)
        r = randint(1, 50)
        qp.drawEllipse(rx, yx, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())