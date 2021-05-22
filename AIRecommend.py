import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap

class Recommend(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # Qlabel
        label1 = QLabel('AI 추천 코디', self)
        label1.setAlignment(Qt.AlignCenter)

        font1 = label1.font()
        font1.setPointSize(30)
        label1.setFont(font1)
        #고른사진
        pixmap = QPixmap('img/top/top11.jpeg')
        #전신진샷
        pixmap2 = QPixmap('img/short.png')

        lbl_img = QLabel()
        lbl_img.setPixmap(pixmap)
        lbl_img2 = QLabel()
        lbl_img2.setPixmap(pixmap2)
        vbox = QGridLayout()



        # Button
        btn1 = QPushButton('다른 추천', self)
        btn1.setCheckable(True)
        btn1.toggle()

        btn2 = QPushButton(self)
        btn2.setText('나가기')
        self.setLayout(vbox)
        btn1.clicked.connect(self.btn1clicked)
        btn2.clicked.connect(self.btn2clicked)
        vbox.addWidget(label1,0,0)
        vbox.addWidget(lbl_img,1,0)
        vbox.addWidget(lbl_img2,1,1)
        vbox.addWidget(btn1, 2, 0)
        vbox.addWidget(btn2,2,1)
        self.setWindowTitle('AI 코디 추천')
        self.resize(400, 300)
        self.show()

    def btn1clicked(self):
        self.close()
        self.win = Recommend()

    def btn2clicked(self):
        self.close()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Recommend()
    sys.exit(app.exec_())