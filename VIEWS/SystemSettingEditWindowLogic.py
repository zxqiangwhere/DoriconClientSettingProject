from PyQt5 import QtGui,QtWidgets,QtCore
import sys
from VIEWS.SystemSettingEditWindow import Ui_Dialog
from MODELS.medmodels import MedHostsetting
from SERVICES.med_hostsetting_services import host_setting_service

class SystemSettingEditWindowLogicClass(QtWidgets.QDialog):

    Signal_Update = QtCore.pyqtSignal()

    def __init__(self,param):
        super(SystemSettingEditWindowLogicClass,self).__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.DataModel = param
        self.initForm()

        self.ui.buttonBox.accepted.connect(self.SaveAction)
        # self.ui.buttonBox.setCenterButtons(True)

    def initForm(self):
        self.ui.lineEdit_SettingName.setText(self.DataModel.setting_name)
        self.ui.lineEdit_SettingKey.setText(self.DataModel.setting_key)
        self.ui.lineEdit_SettingKey.setReadOnly(True)
        self.ui.lineEdit_SettingValue.setText(self.DataModel.setting_value)
        self.ui.lineEdit_SettingDesc.setText(self.DataModel.description)

    def SaveAction(self):
        self.Service = host_setting_service()
        EditItem = self.Service.query(self.DataModel.setting_key)[0]
        if self.ui.lineEdit_SettingName.text() is None or len(self.ui.lineEdit_SettingName.text())==0:
            QtWidgets.QMessageBox.information(self,'提示','配置名称不能为空！',QtWidgets.QMessageBox.Yes)
        else:
            EditItem.setting_name = self.ui.lineEdit_SettingName.text()
            EditItem.setting_value = self.ui.lineEdit_SettingValue.text()
            EditItem.description = self.ui.lineEdit_SettingDesc.text()
            try:
                self.Service.update()
                self.Signal_Update.emit()
                self.accept()
            except:
                replay = QtWidgets.QMessageBox.information(self,'操作提示','更新失败',QtWidgets.QMessageBox.Yes | QtWidgets.QMessageBox.No)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = SystemSettingEditWindowLogicClass('dshjds')
    win.show()
    sys.exit(app.exec_())