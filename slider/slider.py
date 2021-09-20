
style = "font-size:12px;"
# slider-label.py

from PyQt5.QtWidgets import QApplication, QLabel, QSlider
from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap


class SliderLabel(QtWidgets.QWidget):
    def __init__(self, parent=None):
        QtWidgets.QWidget.__init__(self)

        self.setGeometry(800, 600, 800,820)
        self.setWindowTitle('SliderLabel')
        self.slider = QSlider(Qt.Horizontal, self)
        self.slider.setFocusPolicy(Qt.NoFocus)
        self.slider.setGeometry(50,400, 100, 30)
        self.slider.valueChanged.connect(self.changeValue)
        self.label = QLabel(self)
        self.label.setPixmap(QPixmap('F:/picture/1.png'))
        self.label.setGeometry(160, 40, 300, 250)

    def changeValue(self, value):
        pic=[]
        pos = self.slider.value()
        c = [1, 33, 3, 4]
        for k in c:
            image_path = "F:/picture/" + str(k) + ".png"
            pic.append(image_path)
        a=str(pic[0])
        b = str(pic[1])
        c = str(pic[2])
        d = str(pic[3])
        for pos in range(0,30,10):
            a1=str(pos)
            self.label.setPixmap(QPixmap(b))
if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    qb = SliderLabel()
    qb.show()
    sys.exit(app.exec_())