# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SystemSettingEditWindow.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(442, 286)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.lineEdit_SettingName = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_SettingName.setObjectName("lineEdit_SettingName")
        self.horizontalLayout.addWidget(self.lineEdit_SettingName)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_SettingKey = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_SettingKey.setObjectName("lineEdit_SettingKey")
        self.horizontalLayout_2.addWidget(self.lineEdit_SettingKey)
        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_3.addWidget(self.label_4)
        self.lineEdit_SettingValue = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_SettingValue.setObjectName("lineEdit_SettingValue")
        self.horizontalLayout_3.addWidget(self.lineEdit_SettingValue)
        self.gridLayout.addLayout(self.horizontalLayout_3, 2, 0, 1, 1)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_4.addWidget(self.label_5)
        self.lineEdit_SettingDesc = QtWidgets.QLineEdit(Dialog)
        self.lineEdit_SettingDesc.setObjectName("lineEdit_SettingDesc")
        self.horizontalLayout_4.addWidget(self.lineEdit_SettingDesc)
        self.gridLayout.addLayout(self.horizontalLayout_4, 3, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        # self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "编辑配置项"))
        self.label_2.setText(_translate("Dialog", "配置名:"))
        self.label_3.setText(_translate("Dialog", "配置键:"))
        self.label_4.setText(_translate("Dialog", "配置值:"))
        self.label_5.setText(_translate("Dialog", "说  明:"))

