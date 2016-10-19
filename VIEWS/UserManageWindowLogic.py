from PyQt5 import QtGui,QtWidgets
from VIEWS.UserManageWindow import Ui_MainWindow
import sys

class UserManageWindowLogicClass(QtWidgets.QMainWindow):
    def __init__(self):
        super(UserManageWindowLogicClass,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.resize(300,300)


if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = UserManageWindowLogicClass()
    window.show()

    sys.exit(app.exec_())