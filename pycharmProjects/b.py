import sys
from PyQt5 import QtWidgets, QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import csv
from PyQt5.QtCore import *
class picture(QWidget):
    def __init__(self):
        super(picture, self).__init__()

        self.resize(2000, 2000)
        self.setWindowTitle("进程")
        #self.setWindowTitle('ComBox例子')
        # 设置初始界面大小
        #self.resize(300, 200)

        # 实例化QComBox对象
        self.lb1 = QLabel('')
        self.cb = QComboBox(self)
        self.cb.move(10, 10)

        # 单个添加条目
        self.cb.addItem('C')
        # 多个添加条目
        self.cb.addItems(['Java', 'C#', 'PHP'])
        self.cb.currentIndexChanged.connect(self.selectionchange)
        layout = QVBoxLayout()
        layout.addWidget(self.cb)
        layout.addWidget(self.lb1)
        self.setLayout(layout)
        # 信号

        self.label = QLabel(self)
        self.label.setText(" 显示时间")
        self.label.setGeometry(100,100,300,100)

        self.label1 = QLabel(self)
        self.label1.setText(" 显示主体")
        self.label1.setGeometry(300,100, 300, 100)

        self.label2 = QLabel(self)
        self.label2.setText(" 显示地点")
        self.label2.setGeometry(500, 100, 300, 100)

        self.label3 = QLabel(self)
        self.label3.setText(" 显示客体")
        self.label3.setGeometry(700, 100, 300, 100)

        #self.label.setStyleSheet("QLabel{background:white;}"
                               # "QLabel{color:rgb(300,300,300,120);font-size:10px;font-weight:bold;font-family:宋体;}"
                                # )

        btn = QPushButton(self)
        btn.setText("打开文件")
        btn.move(100, 300)
        btn.clicked.connect(self.readFile)



    def selectionchange(self,i):
        self.lb1.setText(self.cb.currentText())
    def readFile(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "选取文件", "C:/", "All Files(*);;Text Files(*.csv)")
        print(filename)

        with open(filename, 'r') as f:
            reader = csv.reader(f)
            for row in reader:#一行为一个列表
                time=row[0]
                place=row[1]
                nvf=row[2]
                self.label.setText(str(time))
                self.label1.setText(str(place))
                self.label1.setText(str(nvf))
                #self.lineEdit.setStyleSheet(row)
        #print(filename, filetype)


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    my = picture()
    my.show()
    sys.exit(app.exec_())
