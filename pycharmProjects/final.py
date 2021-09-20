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

        #主窗口设置
        self.resize(300, 3000)
        self.setWindowTitle("进程")
        self.labela = QLabel(self)
        self.labela.setFixedSize(300,300)
        self.labela.move(2400,300)

        self.labela.setStyleSheet("QLabel{background:white;}"
                                "QLabel{color:rgb(2000,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                )

        #标题设置
        self.textEdit = QtWidgets.QTextEdit(self)
        self.textEdit.setGeometry(QtCore.QRect(400,160,60,32))
        self.textEdit.setObjectName("textEdit")
        self.textEdit.setReadOnly(True)  # 设置为只读，即可以在代码中向textEdit里面输入，但不能从界面上输入,没有这行代码即可以从界面输入
        str = '时间'
        self.textEdit.setText(str)

        self.textEdit1 = QtWidgets.QTextEdit(self)
        self.textEdit1.setGeometry(QtCore.QRect(800, 160, 60, 32))
        self.textEdit1.setObjectName("textEdit")
        self.textEdit1.setReadOnly(True)  # 设置为只读，即可以在代码中向textEdit里面输入，但不能从界面上输入,没有这行代码即可以从界面输入
        str = '主体'
        self.textEdit1.setText(str)

        self.textEdit2 = QtWidgets.QTextEdit(self)
        self.textEdit2.setGeometry(QtCore.QRect(1200, 160, 60, 32))
        self.textEdit2.setObjectName("textEdit")
        self.textEdit2.setReadOnly(True)  # 设置为只读，即可以在代码中向textEdit里面输入，但不能从界面上输入,没有这行代码即可以从界面输入
        str = '地点'
        self.textEdit2.setText(str)

        self.textEdit3 = QtWidgets.QTextEdit(self)
        self.textEdit3.setGeometry(QtCore.QRect(1800, 160, 60, 32))
        self.textEdit3.setObjectName("textEdit")
        self.textEdit3.setReadOnly(True)  # 设置为只读，即可以在代码中向textEdit里面输入，但不能从界面上输入,没有这行代码即可以从界面输入
        str = '客体'
        self.textEdit3.setText(str)

        self.textEdit4 = QtWidgets.QTextEdit(self)
        self.textEdit4.setGeometry(QtCore.QRect(2400, 160, 60, 32))
        self.textEdit4.setObjectName("textEdit")
        self.textEdit4.setReadOnly(True)  # 设置为只读，即可以在代码中向textEdit里面输入，但不能从界面上输入,没有这行代码即可以从界面输入
        str = '图片'
        self.textEdit4.setText(str)



        # 下拉菜单设置
        myframe = QFrame(self)
        myframe.move(100, 50)
        lb1 = QLabel("序列号", myframe)
        lb1.move(0,3)
        self.qcb_pro = QComboBox(myframe)
        self.qcb_pro.move(80,0)
        self.qcb_pro.currentIndexChanged.connect(self.pro_changed)

        self.label = QLabel(self)
        self.label.setGeometry(100,200,400,200)

        #边框大小设置
        self.label1 = QLabel(self)
        self.label1.setGeometry(100,200, 400, 200)

        self.label2 = QLabel(self)
        self.label2.setGeometry(400, 200, 400, 200)

        self.label3 = QLabel(self)
        self.label3.setGeometry(800, 200, 400, 200)

        self.label4 = QLabel(self)
        self.label4.setGeometry(1200, 200, 400, 200)

        self.label5 = QLabel(self)
        self.label5.setGeometry(1800, 200, 400, 200)

        #设置下拉中的元素
        for key in data:
            b = key[0]
            self.qcb_pro.addItem(b, key)

    #设置槽连接
    #文字
    def pro_changed(self,pro_idx):
        #print(self.qcb_pro.itemData(pro_idx))
        b=self.qcb_pro.itemData(pro_idx)
        print(b)
        e=b[0]

        self.label1.setText(b[0])
        self.label2.setText(b[1])
        self.label3.setText(b[2])
        self.label4.setText(b[3])
        self.label5.setText(b[4])

        #图片
        try:
            # image_path = "D://Python//Demo//PycharmProjects-2//picture//" + str(e) + ".png"
            image_path = 'D://Python//Demo//PycharmProjects-2//picture//1.png'
            #jpg = QtGui.QPixmap(image_path).scaled(self.label.width(), self.label.height())
            #self.labela.setPixmap(jpg)
            pix = QtGui.QPixmap(image_path)
            self.labela.setPixmap(pix)
            self.labela.setStyleSheet("border: 2px solid white")
            self.labela.setScaledContents(True)
        except:
            self.labela.setText("无图片")

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
