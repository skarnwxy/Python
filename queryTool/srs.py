# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'srs.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(751, 393)
        self.layoutWidget = QtWidgets.QWidget(Dialog)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 10, 711, 334))
        self.layoutWidget.setObjectName("layoutWidget")
        self.gridlayout = QtWidgets.QGridLayout(self.layoutWidget)
        self.gridlayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.gridlayout.setContentsMargins(0, 0, 0, 0)
        self.gridlayout.setObjectName("gridlayout")
        self.lineEditID = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditID.setObjectName("lineEditID")
        self.gridlayout.addWidget(self.lineEditID, 1, 3, 1, 1)
        self.lineEditFolder = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditFolder.setObjectName("lineEditFolder")
        self.gridlayout.addWidget(self.lineEditFolder, 3, 3, 1, 1)

        self.tableWidget = QtWidgets.QTableWidget(self.layoutWidget)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(116)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setDefaultSectionSize(25)
        self.tableWidget.verticalHeader().setMinimumSectionSize(15)
        self.gridlayout.addWidget(self.tableWidget, 2, 3, 1, 2)

        font = self.tableWidget.horizontalHeader().font()
        font.setBold(True)
        self.tableWidget.horizontalHeader().setFont(font)

        self.pushButtonFolder = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonFolder.setObjectName("pushButtonFolder")
        self.gridlayout.addWidget(self.pushButtonFolder, 3, 4, 1, 1)
        self.labQuery = QtWidgets.QLabel(self.layoutWidget)
        self.labQuery.setObjectName("labQuery")
        self.gridlayout.addWidget(self.labQuery, 2, 1, 1, 1)
        self.labInputFolder = QtWidgets.QLabel(self.layoutWidget)
        self.labInputFolder.setObjectName("labInputFolder")
        self.gridlayout.addWidget(self.labInputFolder, 3, 1, 1, 1)
        self.labInputID = QtWidgets.QLabel(self.layoutWidget)
        self.labInputID.setObjectName("labInputID")
        self.gridlayout.addWidget(self.labInputID, 1, 1, 1, 1)
        self.labInputFile = QtWidgets.QLabel(self.layoutWidget)
        self.labInputFile.setObjectName("labInputFile")
        self.gridlayout.addWidget(self.labInputFile, 0, 1, 1, 1)
        self.pushButtonQuery = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonQuery.setObjectName("pushButtonQuery")
        self.gridlayout.addWidget(self.pushButtonQuery, 1, 4, 1, 1)
        self.pushButtonFile = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButtonFile.setObjectName("pushButtonFile")
        self.gridlayout.addWidget(self.pushButtonFile, 0, 4, 1, 1)
        self.lineEditFile = QtWidgets.QLineEdit(self.layoutWidget)
        self.lineEditFile.setObjectName("lineEditFile")
        self.gridlayout.addWidget(self.lineEditFile, 0, 3, 1, 1)
        self.pushButtonOk = QtWidgets.QPushButton(Dialog)
        self.pushButtonOk.setGeometry(QtCore.QRect(550, 350, 93, 28))
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.pushButtonCacel = QtWidgets.QPushButton(Dialog)
        self.pushButtonCacel.setGeometry(QtCore.QRect(650, 350, 93, 28))
        self.pushButtonCacel.setObjectName("pushButtonCacel")

        self.retranslateUi(Dialog)
        self.pushButtonCacel.clicked.connect(Dialog.close)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.tableWidget.setSortingEnabled(True)
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Dialog", "时间"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Dialog", "地点"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Dialog", "主体"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Dialog", "客体"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("Dialog", "图片"))
        self.pushButtonFolder.setText(_translate("Dialog", "添加文件夹"))
        self.labQuery.setText(_translate("Dialog", "查询结果："))
        self.labInputFolder.setText(_translate("Dialog", "输出文件夹："))
        self.labInputID.setText(_translate("Dialog", "请输入ID："))
        self.labInputFile.setText(_translate("Dialog", "请输入文件："))
        self.pushButtonQuery.setText(_translate("Dialog", "查询"))
        self.pushButtonFile.setText(_translate("Dialog", "添加文件"))
        self.pushButtonOk.setText(_translate("Dialog", "OK"))
        self.pushButtonCacel.setText(_translate("Dialog", "Cancel"))
