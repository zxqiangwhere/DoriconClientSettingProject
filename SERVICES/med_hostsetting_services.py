from DB_HELPER_PACKAGE.dbfactory import get_session
from MODELS import MedDoriconModels


class host_setting_service:
    def __init__(self):
        self.session = get_session()

    def delete(self,item):
        self.session.delete(item)
        self.session.flush()
        self.session.commit()

    def update(self):
        self.session.flush()
        self.session.commit()

    def query(self,setting_key=''):
        '''
        :param setting_key:
        :return: med_hostting list
        '''
        if  setting_key !='':
            items = self.session.query(MedDoriconModels.MedHostsetting).filter(MedDoriconModels.MedHostsetting.setting_key == setting_key).all()
        else:
            items = self.session.query(MedDoriconModels.MedHostsetting).all()
        return items

    def add(self,item):
        self.session.add(item)
        self.session.commit()

if __name__ == '__main__':
    service = host_setting_service()
    items = service.query('FlowServerIP')
    if items is not None:
        for item in items:
            print(item)
            # if 'MCU' in str(item.setting_name):
            #     item.setting_name =  item.setting_name.replace('MCU','多媒体服务器')
            #     service.update()
    else:
        print('None')
