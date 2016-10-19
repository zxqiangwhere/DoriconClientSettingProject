from PyQt5 import QtGui,QtWidgets,QtCore
from VIEWS.SystemSettingWindow import Ui_MainWindow
from VIEWS.UserManageWindowLogic import UserManageWindowLogicClass
from VIEWS.SystemSettingEditWindowLogic import SystemSettingEditWindowLogicClass
import sys
import SERVICES.med_hostsetting_services
from MODELS.MedDoriconModels import MedHostsetting

class SystemSettingWindowLogicClass(QtWidgets.QMainWindow):
    def __init__(self):
        super(SystemSettingWindowLogicClass,self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btn_add.clicked.connect(self.refreshData)
        self.ui.btn_add.clicked.connect(self.AddSettingItem)

        self.setTableViewStyle()
        self.refreshData()

    def setTableViewStyle(self):
        self.ui.tableView.horizontalHeader().setStretchLastSection(True)
        self.ui.tableView.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.ui.tableView.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)

        self.ui.tableView.doubleClicked.connect(self.TableViewSelectioned)

    def AddSettingItem(self):
        self.EditWindow = SystemSettingEditWindowLogicClass(None)
        self.EditWindow.setModal(True)
        self.EditWindow.Signal_Update.connect(self.refreshData)
        self.EditWindow.show()

    def TableViewSelectioned(self):
        index = self.ui.tableView.currentIndex().row()
        SelectedItem = self.Services.query(self.SettingItems[index].setting_key)[0]
        self.EditWindow = SystemSettingEditWindowLogicClass(SelectedItem)
        self.EditWindow.setModal(True)
        self.EditWindow.Signal_Update.connect(self.refreshData)
        self.EditWindow.show()

    def refreshData(self):
        self.Services = SERVICES.med_hostsetting_services.host_setting_service()
        self.LoadData()
        self.InitTableView()

    def LoadData(self):
        self.SettingItems = self.Services.query()

    def InitTableView(self):
        self.DataModel = QtGui.QStandardItemModel()
        self.DataModel.setHorizontalHeaderLabels(['配置名','配置键','配置值','说明'])
        self.ShowColumns = ['setting_name', 'setting_key', 'setting_value', 'description']

        for rowIndex,item in enumerate(self.SettingItems):
            for columnIndex,column in enumerate(self.ShowColumns):
                self.DataModel.setItem(rowIndex,columnIndex,QtGui.QStandardItem(item.to_dict()[column]))
        self.ui.tableView.setModel(self.DataModel)

if __name__ == '__main__':

    app = QtWidgets.QApplication(sys.argv)
    window = SystemSettingWindowLogicClass()
    window.show()

    sys.exit(app.exec_())