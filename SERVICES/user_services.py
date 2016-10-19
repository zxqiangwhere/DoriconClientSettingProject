from DB_HELPER_PACKAGE.dbfactory import get_session,add_item,query_item
from MODELS.testmodels import TUser


def user_insert(item):
    add_item(item)

def user_update(key):
    session = get_session()
    updateuser = session.query(TUser).filter(TUser.id == key).scalar()
    if not updateuser is None:
        updateuser.user_name = 'newname'
        updateuser.extend= 'extend'
        session.commit()
        session.close()
    else:
        print('None')

def user_delete():
    session = get_session()
    user = TUser()
    user.user_name = 'name1'
    deleteuser =  session.query(TUser).filter(TUser.user_name==user.user_name).scalar()
    if not deleteuser is None:
        session.delete(deleteuser)
        session.commit()
        session.close()
    else:
        print('none')
    # return delete_item(item)

def query_user():
    query = query_item(TUser)
    # print('counts:'+str(query.count()))
    print(query.first())
    # print('counts:'+str(query.count()))
    # users = query.order_by(TUser.user_name.desc()).first()
    # # print(len(users))
    # for user in users:
    #     print(user.user_name)
    # print(query.order_by(TUser.user_name).all())
    # user = query.filter(TUser.user_name == 'kaka').first()
    # print(user.id)
    # print(query.filter(TUser.user_name == 'kaka').first())
    # for user in query:
    #     print(user.user_name,user.user_psw)
    # print(query.all())


if __name__=='__main__':
    pass
    # setting = MedHostsetting()
    # setting.serial_no = 3
    # setting.setting_name='test'
    # setting.setting_key='test'
    # setting.setting_value='test'
    # setting.description='test'
    # add_item(setting)
    # # session = get_session()
    # session.add(setting)
    # session.commit()
    # session.close()
    # user_update('132BBB1F134F447086156AD2AD0DA182')
    # user_delete()
    # user =  TUser()
    # user.user_name='name0'
    # user_delete(user)
    # query_user()
    # user = TUser()
    # user.user_name='tom'
    # user.user_psw='123'
    # user_insert(user)