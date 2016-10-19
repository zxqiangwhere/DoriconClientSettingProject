from PyQt5 import QtWidgets
import sys
from VIEWS.DeptDictWindow import Ui_MainWindow

class DeptDictWindowLogicClass(QtWidgets.QMainWindow):
    def __init__(self):
        super(DeptDictWindowLogicClass,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = DeptDictWindowLogicClass()
    window.show()

    sys.exit(app.exec_())