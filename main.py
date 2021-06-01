import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import Qt
from PyQt5 import QtGui
from Clothes import Clothesview
from testImage import Testimage
from Choice import Choice
from PyQt5.QtWidgets import QGraphicsOpacityEffect
import load_model as lm
class MyApp(QWidget):

    def __init__(self):
        self.index = 0
        super().__init__()
        self.initUI()

    def initUI(self):
        #Qlabel
        global label1

        label1 = QLabel('Deep Learning 을\n이용한 코디 추천', self)
        label1.setAlignment(Qt.AlignCenter)

        font1 = label1.font()
        font1.setPointSize(30)

        label1.setFont(font1)
        #Button
        btn = QPushButton('사진 찍기', self)
        btn.setCheckable(True)
        btn.toggle()

        btn1 = QPushButton(self)
        btn1.setText('옷장 보기')

        btn2 = QPushButton('코디 추천',self)
        btn.clicked.connect(self.btnclicked)
        btn1.clicked.connect(self.btn1clicked)
        btn2.clicked.connect(self.btn2clicked)
        layout = QVBoxLayout()
        layout.addWidget(label1)
        layout.addWidget(btn)
        layout.addWidget(btn1)
        layout.addWidget(btn2)
        self.setLayout(layout)
        self.setWindowTitle('AI 코디 추천')
        #창 띄우는 위치
        self.setGeometry(0, 0, 0, 0)
        self.resize(450, 805)
        self.show()
        #사진찍기
    def btnclicked(self):
        model = lm.load_model()
        self.win = Testimage()
        label = lm.labels[lm.predict_output(model,'img/top/top11.jpeg')]
        color = lm.return_color('img/top/top11.jpeg')
        label1.setText('예측된 종류 : '+label+ '\n예측된 색상 :'+ color)
        label1.repaint()

        #옷장
    def btn1clicked(self):
        self.win = Clothesview()

        #코디 추천
    def btn2clicked(self):
        self.win = Choice()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())