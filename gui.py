import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel
from PyQt5.QtGui import QIcon, QPixmap


class App(QWidget):

    def __init__(self):
        super().__init__()
        self.title = 'Advance Driver Asisten System'
        self.left = 0
        self.top = 0
        self.width = 1024
        self.height = 600
        self.initUI()
        self.btnTest()

    def btnTest(self):
        # button tes
        btn_test = QPushButton('CLICK', self)
        # button.setToolTip('This is an example button')
        btn_test.move(50, 50)
        # btn_test.clicked.connect(self.click_show)

    # button open
    def btnOpen(self):
        button = QPushButton('OPEN', self)
        # button.setToolTip('This is an example button')
        button.move(20, 20)
        button.clicked.connect(self.click_open)

    # button exit
    def btnExit(self):
        button = QPushButton('EXIT', self)
        # button.setToolTip('This is an example button')
        button.move(20, 60)
        button.clicked.connect(self.click_exit)

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # self.btnTest()
        self.btnExit()
        self.btnOpen()
        self.show()

    def click_open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName

    def click_exit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
