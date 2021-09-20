#实现确定表中数据的显示
import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import csv
from PyQt5.QtCore import *
#盛放表中所有数据，每行为一个列表
class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()
        self.resize(2000, 2000)
        self.setWindowTitle("进程")

        self.setWindowTitle("labela显示图片")

        self.labela = QLabel(self)
        self.labela.setFixedSize(300, 200)
        self.labela.move(1300, 160)

        self.labela.setStyleSheet("QLabel{background:white;}"
                                 "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                 )
        # 实例化QComBox对象
        self.qcb_pro = QComboBox(self)
        #self.qcb_pro.move(20, 20)
        self.qcb_pro.currentIndexChanged.connect(self.pro_changed)

        self.label = QLabel(self)
        self.label.setGeometry(100,100,300,100)

        self.label1 = QLabel(self)
        self.label1.setGeometry(300,100, 300, 100)

        self.label2 = QLabel(self)
        self.label2.setGeometry(500, 100, 300, 100)

        self.label3 = QLabel(self)
        self.label3.setGeometry(700, 100, 300, 100)

        self.label4 = QLabel(self)
        self.label4.setGeometry(900, 100, 300, 100)

        self.label5 = QLabel(self)
        self.label5.setGeometry(1100, 100, 300, 100)

        layout = QVBoxLayout()
        layout.addWidget(self.qcb_pro)
        layout.addWidget(self.label)
        self.setLayout(layout)
        #self.label.setStyleSheet("QLabel{background:white;}"
                               # "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                # )
        for key in data:
            # print(key, val[0])
            b = key[0]
            self.qcb_pro.addItem(b, key)
    def pro_changed(self,pro_idx):
        #省下拉框改变，先清空市下拉框，然后添加市数据
        #print(self.qcb_pro.itemData(pro_idx))
        b=self.qcb_pro.itemData(pro_idx)
        #print(b)
        e=b[0]
        self.label1.setText(b[0])
        self.label2.setText(b[1])
        self.label3.setText(b[2])
        self.label4.setText(b[3])
        self.label5.setText(b[4])
        try:
            image_path="D://Python//Demo//PycharmProjects-2//picture//"+str(e)+".png"
            #image_path = 'F:/picture/1.png'
            jpg = QtGui.QPixmap(image_path).scaled(self.label.width(), self.label.height())
            self.labela.setPixmap(jpg)
        except:
            self.labela.setText()

if __name__ == "__main__":
    data = []
    filename = "D://Python//Demo//PycharmProjects-2//a.csv"
    with open(filename, 'r') as f:
        reader = csv.reader(f)
        for row in reader:  # 一行为一个列表
            data.append(row)
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())
