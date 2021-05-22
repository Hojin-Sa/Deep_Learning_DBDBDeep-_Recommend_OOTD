import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap
from AIRecommend import Recommend
#추천하기 전 원하는 옷 고르는 클래스
class Choice(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.vbox = QGridLayout()

        cb = QComboBox(self)
        cb.addItem('top')
        cb.addItem('bottom')
        cb.addItem('dress')
        cb.addItem('shoes')
        self.setLayout(self.vbox)
        #창 크
        self.resize(500,400)
        self.lbl_img = QLabel()
        self.lbl_img2 = QLabel()
        cb.activated[str].connect(self.onActivated)
        self.vbox.addWidget(cb,0,0)
        self.setWindowTitle('옷 고르기')
        self.onActivated(cb.currentText())
        self.show()

    def onActivated(self, text):
        self.vbox.removeItem(self.vbox)
        if text == 'top':
            self.top()
        elif text == 'bottom':
            self.bottom()
        elif text == 'dress':
            self.dress()
        elif text == 'shoes':
            self.shoes()

    temp = 1

    def top(self):
        btn_list= []
        for i in range(1, 6):
            st = 'img/top/top1'+str(i)+'.jpeg'
            pixmap = QPixmap(st)
            btn_list.append((i, QPushButton("선택")))
            self.lbl_img = QLabel('lbl_img', self)
            self.lbl_img.setPixmap(pixmap)
            if i % 2 == 0:
                self.vbox.addWidget(self.lbl_img, i-1, 1)
                self.vbox.addWidget(btn_list[i - 1][1], i, 1)
            else:
                self.vbox.addWidget(self.lbl_img, i , 0)
                self.vbox.addWidget(btn_list[i - 1][1], i+1, 0)
            #버튼 추가 코드
        # top의 첫번째 버튼만 눌림 밑에 btn_Clicked를 여러개 만들면 여러개 추가가
        btn_list[0][1].clicked.connect(self.btn_Clicked)

    def btn_Clicked(self):
        self.win = Recommend()

    def bottom(self):
        btn_list = []
        for i in range(1, 6):
            st = 'img/bottom/bottom1' + str(i) + '.jpeg'
            pixmap = QPixmap(st)
            btn_list.append((i, QPushButton("선택")))
            self.lbl_img = QLabel('lbl_img', self)
            self.lbl_img.setPixmap(pixmap)
            if i % 2 == 0:
                self.vbox.addWidget(self.lbl_img, i - 1, 1)
                self.vbox.addWidget(btn_list[i - 1][1], i, 1)
            else:
                self.vbox.addWidget(self.lbl_img, i, 0)
                self.vbox.addWidget(btn_list[i - 1][1], i + 1, 0)

    def dress(self):
        btn_list = []
        for i in range(1, 6):
            st = 'img/dress/dress1' + str(i) + '.jpeg'
            pixmap = QPixmap(st)
            btn_list.append((i, QPushButton("선택")))
            self.lbl_img = QLabel('lbl_img', self)
            self.lbl_img.setPixmap(pixmap)
            if i % 2 == 0:
                self.vbox.addWidget(self.lbl_img, i - 1, 1)
                self.vbox.addWidget(btn_list[i - 1][1], i, 1)
            else:
                self.vbox.addWidget(self.lbl_img, i, 0)
                self.vbox.addWidget(btn_list[i - 1][1], i + 1, 0)

    def shoes(self):
        btn_list = []
        for i in range(1, 6):
            st = 'img/shoes/shoes1' + str(i) + '.jpeg'
            pixmap = QPixmap(st)
            btn_list.append((i, QPushButton("선택")))
            self.lbl_img = QLabel('lbl_img', self)
            self.lbl_img.setPixmap(pixmap)
            if i % 2 == 0:
                self.vbox.addWidget(self.lbl_img, i-1, 1)
                self.vbox.addWidget(btn_list[i - 1][1], i, 1)
            else:
                self.vbox.addWidget(self.lbl_img, i , 0)
                self.vbox.addWidget(btn_list[i - 1][1], i+1, 0)


if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Choice()
   sys.exit(app.exec_())