from PyQt5 import QtWidgets,QtGui
import sys
from VIEWS.DeptDictWindow import Ui_MainWindow
from VIEWS.DeptDictEditWindowLogic import DeptDictEditWindowCls
from SERVICES.dept_dict_services import dept_dict_services_cls

class DeptDictWindowLogicClass(QtWidgets.QMainWindow):
    def __init__(self):
        super(DeptDictWindowLogicClass,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton_Add.clicked.connect(self.AddDept)
        self.ui.pushButton_Search.clicked.connect(self.refreshData)

        self.setTableViewStyle()
        self.refreshData()

    def setTableViewStyle(self):
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableView.doubleClicked.connect(self.TableViewSelectioned)

    def AddDept(self):
        self.EditWindow = DeptDictEditWindowCls()
        self.EditWindow.setModal(True)
        self.EditWindow.Signal_Update.connect(self.refreshData)
        self.EditWindow.show()

    def refreshData(self):
        self.DictService = dept_dict_services_cls()
        self.loadData()
        self.InitTableView()

    def loadData(self):
        self.DeptItems = self.DictService.query(name=self.ui.lineEdit_DeptName.text(),code=self.ui.lineEdit_DeptCode.text())

    def InitTableView(self):
        self.DataModel = QtGui.QStandardItemModel()
        self.DataModel.setHorizontalHeaderLabels(['科室编码','科室名','输入码','备注'])
        self.ShowColumns = ['dept_code','dept_name','input_code','dept_alias']

        for rowIndex,item in enumerate(self.DeptItems):
            for columnIndex,column in enumerate(self.ShowColumns):
                self.DataModel.setItem(rowIndex,columnIndex,QtGui.QStandardItem(item.to_dict()[column]))
        self.ui.tableView.setModel(self.DataModel)

    def TableViewSelectioned(self):
        index = self.ui.tableView.currentIndex().row()
        SelectedItem = self.DeptItems[index]
        self.EditWindow = DeptDictEditWindowCls(SelectedItem)
        self.EditWindow.setModal(True)
        self.EditWindow.Signal_Update.connect(self.refreshData)
        self.EditWindow.show()




if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = DeptDictWindowLogicClass()
    window.show()

    sys.exit(app.exec_())