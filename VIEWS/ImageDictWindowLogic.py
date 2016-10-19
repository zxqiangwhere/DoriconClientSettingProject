from PyQt5 import QtWidgets
import sys
from VIEWS.ImageDictWindow import Ui_MainWindow

class ImageDictWindowLogicClass(QtWidgets.QMainWindow):
    def __init__(self):
        super(ImageDictWindowLogicClass,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = ImageDictWindowLogicClass()
    window.show()

    sys.exit(app.exec_())