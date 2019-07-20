import cv2
import sys
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel, QLineEdit, QMessageBox
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

    # button open
    def btnOpen(self):
        btn_open = QPushButton('OPEN', self)
        # button.setToolTip('This is an example button')
        btn_open.move(20, 20)
        btn_open.clicked.connect(self.click_open)

    # button exit
    def btnExit(self):
        btn_exit = QPushButton('EXIT', self)
        # button.setToolTip('This is an example button')
        btn_exit.move(20, 60)
        btn_exit.clicked.connect(self.click_exit)

    def btnTest(self):
        # button tes
        btn_test = QPushButton('CLICK', self)
        # button.setToolTip('This is an example button')
        btn_test.move(20, 100)
        btn_test.clicked.connect(self.click_show)

    # Create textbox

    def texBox(self):
        self.text_show = QLineEdit(self)
        self.text_show.move(120, 20)
        self.text_show.resize(280, 40)

    def click_show(self):
        textboxValue = self.text_show.text()
        QMessageBox.question(self, 'ADAS', textboxValue,
                             QMessageBox.Ok, QMessageBox.Ok)
        self.text_show.setText("")

    # action click open

    def click_open(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(
            self, "QFileDialog.getOpenFileName()", "", "All Files (*);;Python Files (*.py)", options=options)
        if fileName:
            return fileName
    # initUI

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.btnExit()
        self.btnOpen()
        self.btnTest()
        self.texBox()

        self.show()

    def click_exit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
