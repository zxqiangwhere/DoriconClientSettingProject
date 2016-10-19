from PyQt5 import QtGui,QtWidgets
from VIEWS.AppMainWindow import Ui_MainWindow
from VIEWS.SystemSettingWindowLogic import SystemSettingWindowLogicClass
from VIEWS.DeptDictWindowLogic import DeptDictWindowLogicClass
from VIEWS.ImageDictWindowLogic import ImageDictWindowLogicClass
from VIEWS.AppMainWindow import Ui_MainWindow
import sys

class AppMainWindowLogicClass(QtWidgets.QMainWindow):
    def __init__(self):
        super(AppMainWindowLogicClass,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.actionSystemSetting.triggered.connect(self.ShowSystemSettingWindow)
        self.ui.actionSystemSetting.triggered.connect(lambda :self.showSubWindow('SystemSetting'))
        self.ui.actionDeptDict.triggered.connect(lambda :self.showSubWindow('DeptDict'))
        self.ui.actionImageDict.triggered.connect(lambda :self.showSubWindow('ImageDict'))
        # self.ui.resize(300,300)

    def showSubWindow(self,win):
        if win =='SystemSetting':
            self.SubWindow = SystemSettingWindowLogicClass()
        elif win =='DeptDict':
            self.SubWindow = DeptDictWindowLogicClass()
        elif win == 'ImageDict':
            self.SubWindow = ImageDictWindowLogicClass()
        self.ui.mdiArea.addSubWindow(self.SubWindow)

        self.SubWindow.show()

    # def ShowSystemSettingWindow(self):
    #     # self.SystemSettingWin.show()
    #     self.SystemSettingWin = SystemSettingWindowLogicClass()
    #     self.ui.mdiArea.addSubWindow(self.SystemSettingWin)
    #     self.SystemSettingWin.show()
    #
    # def ShowDeptDictWindow(self):
    #     self.DeptDictWin = DeptDictWindowLogicClass()
    #     self.ui.mdiArea.addSubWindow(self.DeptDictWin)
    #     self.DeptDictWin.show()
    # def ShowImageDictWindow(self):
    #     self.ImageDictWin = ImageDictWindowLogicClass()
    #     self.ui.mdiArea.addSubWindow(self.ImageDictWin)
    #     self.ImageDictWin.show()
    #     print(self.ui.mdiArea.subWindowList()[0].__doc__)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = AppMainWindowLogicClass()
    window.show()

    sys.exit(app.exec_())