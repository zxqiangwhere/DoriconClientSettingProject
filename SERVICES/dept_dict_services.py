from DB_HELPER_PACKAGE.dbfactory import get_session
from MODELS.MedCommModels import MedDeptDict

class dept_dict_services_cls:
    def __init__(self):
        self.session = get_session()

    def delete(self,item):
        self.session.delete(item)
        self.session.flush()
        self.session.commit()

    def update(self):
        self.session.flush()
        self.session.commit()

    def GetMaxSerialNo(self):
        MaxSerialNo = self.session.query(MedDeptDict.serial_no).order_by(MedDeptDict.serial_no.desc()).first()[0]
        if MaxSerialNo is None:
            return 1000
        else:
            return int(MaxSerialNo)+1

    def query(self,key='',name='',code=''):
        if key!='':
            query = self.session.query(MedDeptDict).filter(MedDeptDict.serial_no == key)
        elif name!='':
            query = self.session.query(MedDeptDict).filter(MedDeptDict.dept_name.like('%'+name+'%'))
        elif code !='':
            query = self.session.query(MedDeptDict).filter(MedDeptDict.dept_code.like('%' + code + '%'))
        else:
            query = self.session.query(MedDeptDict).order_by(MedDeptDict.serial_no.desc())
        return query.all()

    def add(self,item):
        self.session.add(item)
        self.session.commit()

if __name__ == '__main__':
    service = dept_dict_services_cls()
    print(service.GetMaxSerialNo())
    # items  = service.query(name='呼吸')
    # for item in items:
    #     print(item)