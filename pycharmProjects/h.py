from PyQt5.Qt import *

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("")
        self.resize(500,500)

        self.label2 = QLabel(self)
        self.label2.setText(" 显示地点")
        self.label2.setGeometry(500, 100, 300, 100)


        #后期这个字典可以从数据库中传入
        self.province = [["1","2"],["3","4"]]
        self.setup_ui()

    def setup_ui(self):
        #1.创建省下拉框，修改一些显示尺寸（这个可以自行调节）
        qcb_pro = QComboBox(self)
        qcb_pro.resize(80,25)
        qcb_pro.move(100,100)
        self.qcb_pro = qcb_pro

        layout = QVBoxLayout()
        layout.addWidget(self.qcb_pro)
        layout.addWidget(self.label2)
        self.setLayout(layout)
        #3.创建市下拉选择框

        # 4.为下拉框绑定触发事件,currentIndexChanged信号有两个方法，指定获取int的这个方法
        qcb_pro.currentIndexChanged.connect(self.pro_changed)


        # 2.为省下拉框填充数据，可根据从数据库中检索出的数据，动态填充
        for key in self.province:
            #print(key, val[0])
            b=key[0]
            a = key[1]
            qcb_pro.addItem(b,a)

    def pro_changed(self,pro_idx):
        #省下拉框改变，先清空市下拉框，然后添加市数据
        #print(self.qcb_pro.itemData(pro_idx))
        b=self.qcb_pro.itemData(pro_idx)
        print(b)
        self.label2.setText(b)
if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec())