from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DB_CONNECTION_STRING = 'oracle+cx_oracle://testuser:testuser@127.0.0.1/orcl'
Base = declarative_base()

DB_CONNECTION_STRING = 'oracle+cx_oracle://system:docare@192.168.18.86/orcl'

enginner = create_engine(DB_CONNECTION_STRING,echo=True)
db_session = sessionmaker(bind=enginner)
# session = db_session()

def add_item(item):
    '''
    model插入公共方法
    :param item: 掺入的model
    :return: 返回success/error
    '''
    result = 'success'
    try:
        session = db_session()
        session.add(item)
        session.commit()
    except:
        session.rollback()
        result = 'error'
    finally:
        session.close()
    return result

def delete_item(item):
    result = True
    try:
        session = db_session()
        session.delete(item)
        session.commit()
    except:
        session.rollback()
        result = False
    finally:
        session.close()
    return result

def query_item(obj):
    '''

    :param item:
    :return:
    '''
    session = db_session()
    return session.query(obj)
    # try:
    #     session = db_session()
    #     return session.query(item)
    # except:
    #     return 'query error'
    # finally:
    #     session.close()


def get_session():
    return db_session()

# def close_seesion():


def init_db():
    Base.metadata.create_all(enginner)
def drop_db():
    Base.metadata.drop_all(enginner)


# if __name__=='__main__':
#     # user = TUser()
#     # # import uuid
#     # # user.id =uuid.uuid1()
#     # user.user_name='kaka'
#     # user.user_psw='123'
#     for i in range(100):
#         user = TUser()
#         user.user_name='name'+str(i)
#         user.user_psw='123'
#         session.add(user)
#
#     # session.add(user)
#     session.commit()
#     session.close()