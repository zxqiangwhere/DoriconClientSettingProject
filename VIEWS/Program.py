from PyQt5 import QtCore, QtGui, QtWidgets
from VIEWS.login import Ui_Dialog
import sys

class Main(QtWidgets.QDialog):
    def __init__(self):
        super(Main,self).__init__()

        self.ui = Ui_Dialog()
        self.ui.setupUi(self)

        self.ui.pushButton_2.clicked.connect(self.Cancel)
        self.ui.pushButton.clicked.connect(self.login)

    def login(self):
        username = self.ui.lineEdit_username.text()
        psw = self.ui.lineEdit_Psw.text()
        if len(username) ==0 or len(psw)==0:
            QtWidgets.QMessageBox.information(self,'Error','用户名或密码为空！',QtWidgets.QMessageBox.Yes)
        else:
            if username =='admin' and psw == '123':
                self.accept()
                # QtWidgets.QMessageBox.information(self,'tip','Login Success')
                from VIEWS.AppMainWindowLogic import AppMainWindowLogicClass
                self.AppMainWindow = AppMainWindowLogicClass()
                self.AppMainWindow.show()
            else:
                QtWidgets.QMessageBox.information(self,'Error','用户名或密码错误',QtWidgets.QMessageBox.Yes)

    def Cancel(self):
        QtWidgets.QDialog.exec()


if __name__=='__main__':
    app = QtWidgets.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())
