import sys
from random import randint

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import QtCore


class MyWidget(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.setMouseTracking(True)

    def initUI(self):
        self.setGeometry(500, 300, 450, 500)
        self.setWindowTitle('Убегающая кнопка')
        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(QtCore.QRect(50, 50, 70, 25))
        self.pushButton.setText("Нажми меня")

    def mouseMoveEvent(self, event):
        if self.pushButton.x() - 10 <= event.x() <= self.pushButton.x() + 80 and\
                        self.pushButton.y() - 10 <= event.y() <= self.pushButton.y() + 40:
            self.pushButton.move(randint(0, 380), randint(0, 475))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec())