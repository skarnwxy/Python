
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
        if pos == 0:
            self.label.setPixmap(QPixmap(a))
        elif 0 < pos <= 30:
            self.label.setPixmap(QPixmap(b))
        elif 30 < pos < 200:
            self.label.setPixmap(QPixmap(c))
        else:
            self.label.setPixmap(QPixmap(d))


if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    qb = SliderLabel()
    qb.show()
    sys.exit(app.exec_())