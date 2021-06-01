import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPixmap

# 옷장 클래스
class Clothesview(QWidget):

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
        # 창 크기
        self.setGeometry(0, 0, 0, 0)
        self.resize(450, 805)
        self.lbl_img = QLabel()
        self.lbl_img2 = QLabel()
        cb.activated[str].connect(self.onActivated)
        self.vbox.addWidget(cb,0,0)
        self.setWindowTitle('옷장')
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

    def top(self):
        for i in range(1, 7):
            st = 'img/top/top1'+str(i)+'.jpeg'
            pixmap = QPixmap(st)
            self.lbl_img = QLabel('lbl_img', self)
            self.lbl_img.setPixmap(pixmap)
            if i % 2 == 0:
                self.vbox.addWidget(self.lbl_img,int((i-1)/2+1),1)
            else:
                self.vbox.addWidget(self.lbl_img, int((i-1)/2+1), 0)

    def bottom(self):
        for i in range(1, 7):
            st = 'img/bottom/bottom1' + str(i) + '.jpeg'
            pixmap = QPixmap(st)
            self.lbl_img = QLabel('lbl_img', self)
            #self.lbl_img.resize(100)
            self.lbl_img.setPixmap(pixmap)
            if i % 2 == 0:
                self.vbox.addWidget(self.lbl_img, int((i - 1) / 2 + 1), 1)
            else:
                self.vbox.addWidget(self.lbl_img, int((i - 1) / 2 + 1), 0)

    def dress(self):
        for i in range(1, 7):
            st = 'img/dress/dress1' + str(i) + '.jpeg'
            pixmap = QPixmap(st)
            self.lbl_img = QLabel('lbl_img', self)
            self.lbl_img.setPixmap(pixmap)
            if i % 2 == 0:
                self.vbox.addWidget(self.lbl_img, int((i - 1) / 2 + 1), 1)
            else:
                self.vbox.addWidget(self.lbl_img, int((i - 1) / 2 + 1), 0)

    def shoes(self):
        for i in range(1, 7):
            st = 'img/shoes/shoes1' + str(i) + '.jpeg'
            pixmap = QPixmap(st)
            self.lbl_img = QLabel('lbl_img', self)
            self.lbl_img.setPixmap(pixmap)
            if i % 2 == 0:
                self.vbox.addWidget(self.lbl_img, int((i - 1) / 2 + 1), 1)
            else:
                self.vbox.addWidget(self.lbl_img, int((i - 1) / 2 + 1), 0)

if __name__ == '__main__':
   app = QApplication(sys.argv)
   ex = Clothesview()
   sys.exit(app.exec_())