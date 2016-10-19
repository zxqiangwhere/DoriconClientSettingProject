# coding: utf-8
from sqlalchemy import Column, String, text,Numeric
from sqlalchemy.ext.declarative import declarative_base
from DB_HELPER_PACKAGE.dbfactory import Base

metadata = Base.metadata

class MedHostsetting(Base):
    __tablename__ = 'med_hostsettings'

    hostsetting_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    serial_no = Column(Numeric(3, 0, asdecimal=False))
    setting_name = Column(String(50))
    setting_key = Column(String(50))
    setting_value = Column(String(500))
    description = Column(String(100))
    memo = Column(String(100))


class TUser(Base):
    __tablename__ = 't_users'

    id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    user_name = Column(String(36), nullable=False)
    user_psw = Column(String(36), nullable=False)
    extend = Column(String(36))

    # def __repr__(self):
    #     # result = {}
    #     # for c in self.__table__.columns:
    #     #     result[c.name] = self.c.name
    #     # return result
    #     # return 'username:'+self.user_name+', psw:'+self.user_psw
    #     return str({c.name:getattr(self,c.name) for c in self.__table__.columns})
