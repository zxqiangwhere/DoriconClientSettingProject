import sys
from PyQt5 import QtWidgets,QtCore
from VIEWS.DeptDictEditWindow import Ui_Dialog
from MODELS.MedCommModels import MedDeptDict
from SERVICES.dept_dict_services import dept_dict_services_cls

class DeptDictEditWindowCls(QtWidgets.QDialog):

    Signal_Update = QtCore.pyqtSignal()

    def __init__(self,param=None):
        super(DeptDictEditWindowCls,self).__init__()
        self.ui =Ui_Dialog()
        self.ui.setupUi(self)

        self.DeptService = dept_dict_services_cls()

        if param is not None:
            self.EditModel = param
            self.InitForm()
            self.ui.buttonBox.accepted.connect(self.SaveAction)
        else:
            self.ui.buttonBox.accepted.connect(self.AddAction)


    def InitForm(self):
        self.ui.lineEdit_Name.setText(self.EditModel.dept_name)
        self.ui.lineEdit_Code.setText(self.EditModel.dept_code)
        self.ui.lineEdit_InputCode.setText(self.EditModel.input_code)

    def ValidateForm(self):
        message = None
        if self.ui.lineEdit_Code.text() is None or len(self.ui.lineEdit_Code.text()) == 0:
            message = "科室编码不能为空"
        if self.ui.lineEdit_Name.text() is None or len(self.ui.lineEdit_Name.text()) == 0:
            message = "科室名称不能为空"
        return message

    def AddAction(self):
        validatemessage = self.ValidateForm()
        if validatemessage is None:
            AddItem = MedDeptDict()
            AddItem.input_code = self.ui.lineEdit_InputCode.text()
            AddItem.dept_code = self.ui.lineEdit_Code.text()
            AddItem.dept_name = self.ui.lineEdit_Name.text()
            AddItem.serial_no = self.DeptService.GetMaxSerialNo()
            try:
                self.DeptService.add(AddItem)
                self.Signal_Update.emit()
                self.accept()
            except:
                QtWidgets.QMessageBox.information(self,'提示','添加失败',QtWidgets.QMessageBox.Yes)
        else:
            QtWidgets.QMessageBox.information(self,'提示',validatemessage,QtWidgets.QMessageBox.Yes)

    def SaveAction(self):
        EditItem = self.DeptService.query(key=self.EditModel.serial_no)[0]
        validatemessage = self.ValidateForm()
        if validatemessage is None:
            EditItem.dept_code = self.ui.lineEdit_Code.text()
            EditItem.dept_name = self.ui.lineEdit_Name.text()
            EditItem.input_code = self.ui.lineEdit_InputCode.text()
            try:
                self.DeptService.add(EditItem)
                self.Signal_Update.emit()
                self.accept()
            except:
                QtWidgets.QMessageBox.information(self, '提示', '修改失败', QtWidgets.QMessageBox.Yes)
        else:
            QtWidgets.QMessageBox.information(self,'提示',validatemessage,QtWidgets.QMessageBox.Yes)



if __name__ =='__main__':
    app = QtWidgets.QApplication(sys.argv)
    win = DeptDictEditWindowCls()
    win.show()
    app.exit(app.exec_())