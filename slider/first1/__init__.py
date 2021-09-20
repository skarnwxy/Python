#存在问题，输错闪退，不能显示多张图片
import first1.whole as fir
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import csv
from PyQt5.QtCore import *
from os import listdir
from PIL import Image

class SliderDemo(QWidget,fir.Ui_Form):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setupUi(self)
        self.setWindowTitle("first")
        self.openbtn.clicked.connect(self.readFile)
        #self.oppbtn_3.clicked.connect(self.appFile)
        self.insbtn.clicked.connect(self.insertFile)
        self.Slider.valueChanged.connect(self.changeValue)
        self.label.setStyleSheet("border: 2px solid white")
        self.label.setScaledContents(True)

    def readFile(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "选取文件", "C:/", "All Files(*);;Text Files(*.csv)")
        #print(filename)
        self.openet.setText(filename)
    def insertFile(self):
        data=[]
        xulie = self.etid.text()
        filename=self.openet.text()
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:  # 一行为一个列表
                data.append(row)
            m=[]
            for i in range(0,len(data)):
                if xulie==data[i][0]:
                    b=(data[i][2])+data[i][3]
                    m.append(b)
                    c=''
                    for i in m:
                        c=c+i+'\n'+"\n"
                        d=c
                    image_path = "F:/picture/" + str(xulie) + ".png"
                    pix = QtGui.QPixmap(image_path)
            self.label.setPixmap(pix)
            self.ettext.setText(d)


    def changeValue(self, value):
        d1=[]
        d2=[]
        d3=[]
        d4=[]
        d5=[]
        pic=[]
        xulie = self.etid.text()
        filename = self.openet.text()
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:  # 一行为一个列表
                k=row[0]
                d1.append(row[0])
                d2.append(row[1])
                d3.append(row[2])
                d4.append(row[3])
                d5.append(row[4])
                image_path = "F:/picture/" + str(k) + ".png"
                pic.append(image_path)
        pos = self.Slider.value()
        if pos == 0:
            d11=str(d1[0])
            d12= str(d2[0])
            d13 =str(d3[0])
            d14 =str(d4[0])
            pic1=str(pic[1])
            pix = QtGui.QPixmap(pic1)
            self.label_2.setPixmap(QPixmap(pix))
            self.timeet.setText(str(d12))
            self.zhutiet.setText(str(d13))
            self.placeet.setText(str(d14))

        elif 0 < pos <= 1:
            d11 = str(d1[1])
            d12 = str(d2[1])
            d13 = str(d3[1])
            d14 = str(d4[1])
            pic1 = str(pic[2])
            pix = QtGui.QPixmap(pic1)
            self.label_2.setPixmap(QPixmap(pix))
            self.timeet.setText(str(d12))
            self.zhutiet.setText(str(d13))
            self.placeet.setText(str(d14))
            #self.label_2.setPixmap(QPixmap('F:/picture/33.png'))
        elif 30 < pos < 200:
            self.label_2.setPixmap(QPixmap('F:/picture/29.png'))
        else:
            self.label_2.setPixmap(QPixmap('F:/picture/4.png'))
    def appFile(self):
        data=[]
        xulie = self.etid.text()
        filename=self.openet.text()
        with open(filename, 'r', encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:  # 一行为一个列表
                data.append(row)




if __name__ == '__main__':
    app = QApplication(sys.argv)
    sl = SliderDemo()
    sl.show()
    sys.exit(app.exec_())
