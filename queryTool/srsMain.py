# -*- coding:utf-8 -*-
# 后端：控件交互

from PyQt5 import QtWidgets
from srs import Ui_Dialog

from PyQt5.QtCore import QFile
from PyQt5.QtWidgets import QFileDialog
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import Qt

# import pandas as pd
import xlrd

class mywindow(QtWidgets.QWidget, Ui_Dialog):
    def __init__(self):
        super(mywindow, self).__init__()
        self.setupUi(self)

        # 添加文件——读
        self.pushButtonFile.clicked.connect(self.readFile)
        # 查询——查
        self.pushButtonQuery.clicked.connect(self.QueryInformation)

        # 添加文件夹——写
        self.pushButtonFolder.clicked.connect(self.writeFolder)
        # 保存结果——存
        self.pushButtonOk.clicked.connect(self.SaveResult)

    # 添加文件——读
    def readFile(self):
        # ①：将文件路径添加至编辑行
        filename, filetype =QFileDialog.getOpenFileName(self, "选取文件", "D:/Python/Demo/PycharmProjects-2", "All Files(*);;Text Files(*.xlsx)")
        print(filename, filetype)
        self.lineEditFile.setText(filename)

        # ②：将文件内容写入表格中
        # 打开文件
        workbook = xlrd.open_workbook(filename)

        sheet1 = workbook.sheet_by_index(0)  # sheet索引从0开始
        cols = sheet1.col_values(1) # 获取列数

        # 获取整行和整列的值（数组）
        for i in range(1, len(cols)):
            # 获取excel每行内容
            rowslist = sheet1.row_values(i)
            # 插入行
            row = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row)

            for j in range(len(rowslist)):
                # 把数据写入tablewidget中
                newItem = QTableWidgetItem(rowslist[j])

                # 将写入的内容居中
                if j != len(rowslist) - 1:
                    newItem.setTextAlignment(Qt.AlignHCenter | Qt.AlignVCenter)
                self.tableWidget.setItem(row, j, newItem)

    # 查询——查
    def QueryInformation(self):
        workbook = xlrd.open_workbook('D:/Python/Demo/PycharmProjects-2/test1.xlsx')

    # 添加文件夹——写
    def writeFolder(self):
        # 选取文件夹
        foldername = QFileDialog.getExistingDirectory(self, "选取文件夹", "C:/")
        print(foldername)
        self.lineEditFolder.setText(foldername)

    # 保存结果——存
    def SaveResult(self):
        try:
            # 获取文件路径
            file_path = self.lineEditFile.text()
            # 获取文件夹路径
            folder_path = self.lineEdit_2.text()

            # 读取文件
            my_df = pd.read_csv(file_path, encoding='mbcs')

            # 进行csv输出
            my_df.to_csv(folder_path + '/result.csv')
            success_result = r'转换成功！'
            self.label_3.setText(success_result)

        except:
            fail_result = r'转换失败！'
            self.label_3.setText(fail_result)

if __name__=="__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ui = mywindow()
    ui.show()
    sys.exit(app.exec_())