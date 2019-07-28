import cv2
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QFileDialog, QPushButton, QLabel, QLineEdit, QMessageBox, QVBoxLayout, QMainWindow
from PyQt5.QtGui import QIcon, QPixmap, QImage

fname = ""


class App(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = 'Advance Driver Asisten System'
        self.left = 0
        self.top = 0
        self.width = 1024
        self.height = 600
        self.initUI()

    # initUI
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # self.central_widget = QWidget()
        # self.button_frame = QPushButton('Acquire Frame', self.central_widget)
        # self.button_movie = QPushButton('Start Movie', self.central_widget)
        # self.layout = QVBoxLayout(self.central_widget)
        # self.layout.addWidget(self.button_frame)
        # self.layout.addWidget(self.button_movie)
        # self.setCentralWidget(self.central_widget)
        self.btnOpen()
        self.btnGray()
        self.btnExit()
        self.label_img_ori()
        self.title_img_ori()
        self.show()

    # button open

    def btnOpen(self):
        btn_open = QPushButton('OPEN', self)
        # button.setToolTip('This is an example button')
        btn_open.move(20, 20)
        btn_open.clicked.connect(self.click_open)

    def btnGray(self):
        btn_open = QPushButton('GRAY', self)
        # button.setToolTip('This is an example button')
        btn_open.move(20, 60)
        btn_open.clicked.connect(self.imGray)

    # button exit
    def btnExit(self):
        btn_exit = QPushButton('EXIT', self)
        # button.setToolTip('This is an example button')
        btn_exit.move(20, 100)
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

    def title_img_ori(self):
        self.title_img_ori = QLabel(self)
        self.title_img_ori.setText("Captured Image")
        self.title_img_ori.move(200, 10)

    def label_img_ori(self):
        self.label_img_ori = QLabel(self)
        self.label_img_ori.setPixmap(QPixmap())
        self.label_img_ori.resize(250, 250)
        self.label_img_ori.move(200, 40)
        self.label_img_ori.setScaledContents(True)

    # action click open
    def click_open(self):
        global fname
        # options = QFileDialog.Options()
        # options |= QFileDialog.DontUseNativeDialog
        # fname, _ = QFileDialog.getOpenFileName(
        #     self, "QFileDialog.getOpenFileName()", "", "All Files (*)", options=options)

        fname, filter = QFileDialog.getOpenFileName(
            self, 'Open File', "Image Files(*)")

        if fname:
            self.loadImage(fname)

    def loadImage(self, fname):
        self.img_ori = cv2.imread(fname, 1)
        self.displayImageOri()

    def imGray(self):
        self.img_ori = cv2.imread(fname, 1)
        self.img_gray = cv2.cvtColor(self.img_ori, cv2.COLOR_BGR2GRAY)
        self.height, self.width = self.img_gray.shape[:2]

        qformat = QtGui.QImage.Format_Grayscale8

        img = QtGui.QImage(self.img_gray, self.width,
                           self.height, self.img_gray.strides[0], qformat)

        img = QPixmap.fromImage(img)
        self.label_img_ori.setPixmap(img)
        self.label_img_ori.setAlignment(QtCore.Qt.AlignCenter)

    def displayImageOri(self):
        qformat = QImage.Format_RGB888
        self.height, self.width = self.img_ori.shape[:2]

        img = QtGui.QImage(self.img_ori.data, self.width,
                           self.height, self.img_ori.strides[0], qformat)

        img = img.rgbSwapped()

        img = QPixmap.fromImage(img)
        self.label_img_ori.setPixmap(img)
        self.label_img_ori.setAlignment(QtCore.Qt.AlignCenter)

    def click_exit(self):
        self.close()


if __name__ == '__main__':
    app = QApplication([])
    ex = App()
    app.exit(app.exec_())
