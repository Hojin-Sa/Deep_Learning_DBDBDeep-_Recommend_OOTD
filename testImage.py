import cv2
import sys
import load_model as lm

from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtCore import Qt
# 사진찍는 클래스
class Testimage(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.output = ""
    def initUI(self):
        cap = cv2.VideoCapture(0)

        while True:
            ret, frame = cap.read()

            if not ret:
                break
            #파일 사이즈
            #img_resize = cv2.resize(frame, dsize=(400,800), interpolation=cv2.INTER_AREA)
            img_crop = frame[35:1381,375:825].copy()

            cv2.imshow('사진 찍기', img_crop)
            #esc누르면 사진찍히며 종료 + 27이 esc 유니코드

            if cv2.waitKey(1) == 27:
                #img/20.jpeg 경로설정, 파일이름결정 가능
                img_crop = cv2.resize(img_crop, (200, 200))
                cv2.imwrite('img/top/top11.jpeg', img_crop, params=[cv2.IMWRITE_PNG_COMPRESSION, 0])
                cap.release()
                # self.output = lm.labels[lm.predict_output(model,'img/top/top11.jpeg')]
                # print(self.output)
                cv2.destroyWindow('사진 찍기')
                break


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Testimage()
    sys.exit(app.exec_())
