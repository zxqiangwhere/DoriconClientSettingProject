# coding: utf-8
from sqlalchemy import Column, DateTime, Numeric, String, text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base
from DB_HELPER_PACKAGE.dbfactory import Base


metadata = Base.metadata


class MedCommDict(Base):
    __tablename__ = 'med_comm_dict'

    dict_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    app_id = Column(String(36))
    groupname = Column(String(50))
    groupid = Column(String(36))
    item_key = Column(String(50))
    item_value = Column(String(50))
    description = Column(String(50))
    serial_no = Column(Numeric(6, 0, asdecimal=False))
    isgroup = Column(Numeric(1, 0, asdecimal=False), server_default=text("""\
0
"""))


class MedHostsetting(Base):
    __tablename__ = 'med_hostsettings'

    hostsetting_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    serial_no = Column(Numeric(3, 0, asdecimal=False))
    setting_name = Column(String(50))
    setting_key = Column(String(50))
    setting_value = Column(String(500))
    description = Column(String(100))
    memo = Column(String(100))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}
    def getcolumns(self):
        objcolumns = []
        for c in self.__table__.columns:
            objcolumns.append(str(c.name))
        return objcolumns


class MedItemImage(Base):
    __tablename__ = 'med_item_image'

    img_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    app_id = Column(String(36))
    open_img_path = Column(String(150))
    close_img_path = Column(String(150))
    status = Column(String(1), server_default=text("1"))
    description = Column(String(200))


class MedLogRecord(Base):
    __tablename__ = 'med_log_record'

    logid = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    app_id = Column(String(36), nullable=False)
    type = Column(String(36))
    action = Column(String(36))
    content = Column(String(200), nullable=False)
    logtime = Column(DateTime, nullable=False)
    user_id = Column(String(36))
    description = Column(String(100))


class MedOperatingRoomDevice(Base):
    __tablename__ = 'med_operating_room_device'

    device_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    room_no = Column(String(4))
    dept_code = Column(String(8))
    name = Column(String(20))
    type = Column(String(20))
    serial_no = Column(Numeric(5, 0, asdecimal=False))
    status = Column(String(1))
    channel = Column(String(3))
    screendevice_id = Column(String(36))
    img_id = Column(String(36))
    desciption = Column(String(80))
    memo = Column(String(50))


class MedOperatingRoomext(Base):
    __tablename__ = 'med_operating_roomext'

    room_no = Column(String(4), primary_key=True, nullable=False)
    dept_code = Column(String(8), primary_key=True, nullable=False)
    patient_id = Column(String(20))
    visit_id = Column(Numeric(5, 0, asdecimal=False))
    oper_id = Column(Numeric(2, 0, asdecimal=False))
    use_status = Column(String(1), server_default=text("1"))
    live_status = Column(String(1), server_default=text("0"))
    description = Column(String(50))
    lock_flag = Column(Numeric(1, 0, asdecimal=False), server_default=text("""\
0
"""))


class MedOperatingRoomuser(Base):
    __tablename__ = 'med_operating_roomusers'

    roomuser_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    user_id = Column(String(36), nullable=False)
    room_no = Column(String(20))
    dept_code = Column(String(20))
    roomuser_type = Column(String(20))
    use_status = Column(String(20))
    description = Column(String(100))


class MedOperationEventconfig(Base):
    __tablename__ = 'med_operation_eventconfig'

    eventconfig_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    type = Column(String(2), server_default=text("0"))
    item_code = Column(String(36))
    display_type = Column(String(2))
    line_color = Column(String(20), server_default=text("'Red'"))
    point_graph = Column(String(20))
    point_graph_color = Column(String(20))
    point_graph_fill_color = Column(String(20))
    word_color = Column(String(20), server_default=text("'Black'"))
    word_size = Column(NullType, server_default=text("8"))
    use_status = Column(String(2), server_default=text("1"))
    description = Column(String(50))
    sequenceno = Column(Numeric(2, 0, asdecimal=False), server_default=text("99"))
    scalemin = Column(NullType, server_default=text("0"))
    scalemax = Column(NullType, server_default=text("260"))
    majorstep = Column(NullType, server_default=text("20"))
    minorstep = Column(NullType, server_default=text("10"))
    minspace = Column(NullType, server_default=text("30"))
    moremajortics = Column(Numeric(2, 0, asdecimal=False), server_default=text("5"))
    use_axissetting = Column(String(2), server_default=text("""\
1
"""))


class MedOperationObserve(Base):
    __tablename__ = 'med_operation_observe'

    observe_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    user_id = Column(String(36))
    room_no = Column(String(20))
    dept_code = Column(String(20))
    patient_id = Column(String(20))
    visit_id = Column(Numeric(2, 0, asdecimal=False))
    oper_id = Column(Numeric(2, 0, asdecimal=False))
    applicant = Column(String(36))
    apply_time = Column(DateTime)
    apply_status = Column(String(4))
    approver = Column(String(36))
    approval_time = Column(DateTime)
    description = Column(String(200))


class MedOperationPermission(Base):
    __tablename__ = 'med_operation_permission'

    orpermission_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    user_id = Column(String(36))
    patient_id = Column(String(20))
    visit_id = Column(Numeric(2, 0, asdecimal=False))
    oper_id = Column(Numeric(2, 0, asdecimal=False))
    description = Column(String(100))


class MedOperationPhoto(Base):
    __tablename__ = 'med_operation_photos'

    photo_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    patient_id = Column(String(20), nullable=False)
    visit_id = Column(Numeric(2, 0, asdecimal=False))
    oper_id = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    upload_status = Column(String(4), nullable=False)
    photo_person = Column(String(36))
    extend1 = Column(String(50))
    extend2 = Column(String(50))
    dept_code = Column(String(20))
    room_no = Column(String(4))


class MedOperationPhotosDetail(Base):
    __tablename__ = 'med_operation_photos_details'

    details_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    photo_id = Column(String(36), nullable=False)
    file_no = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    file_name = Column(String(50), nullable=False)
    file_path = Column(String(255))
    server_file_name = Column(String(50))
    server_file_path = Column(String(255))
    upload_status = Column(String(4), nullable=False)
    extend1 = Column(String(50))
    extend2 = Column(String(50))


class MedOperationRecord(Base):
    __tablename__ = 'med_operation_record'

    record_code = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    status = Column(String(4))
    upload_status = Column(String(4))
    start_time = Column(DateTime)
    end_time = Column(DateTime)
    record_person = Column(String(36))
    extend1 = Column(String(50))
    extend2 = Column(String(50))


class MedOperationRecordChannel(Base):
    __tablename__ = 'med_operation_record_channel'

    record_code = Column(String(36), primary_key=True, nullable=False)
    user_code = Column(String(36), primary_key=True, nullable=False)
    channel_no = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    user_type = Column(Numeric(2, 0, asdecimal=False))
    dept_code = Column(String(20))
    room_no = Column(String(4))
    channel_name = Column(String(20))
    extend1 = Column(String(30))
    extend2 = Column(String(30))


class MedOperationRecordDetail(Base):
    __tablename__ = 'med_operation_record_details'

    details_code = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    record_code = Column(String(36), nullable=False)
    file_no = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    fiel_name = Column(String(80))
    file_path = Column(String(255))
    server_file_name = Column(String(80))
    server_file_path = Column(String(255))
    upload_status = Column(String(4), nullable=False)
    start_time = Column(DateTime, nullable=False)
    end_time = Column(DateTime)
    extend1 = Column(String(50))
    extend2 = Column(String(50))
    file_size = Column(Numeric(5, 0, asdecimal=False))


class MedOperationRecordPatinfo(Base):
    __tablename__ = 'med_operation_record_patinfo'

    patientinfo_code = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    record_code = Column(String(36))
    patient_id = Column(String(20))
    visit_id = Column(Numeric(2, 0, asdecimal=False))
    oper_id = Column(Numeric(2, 0, asdecimal=False))
    dept_code = Column(String(20))
    room_no = Column(String(4))
    extend1 = Column(String(30))
    extend2 = Column(String(30))


class MedOperationSummary(Base):
    __tablename__ = 'med_operation_summary'

    summary_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    summary_name = Column(String(50), nullable=False)
    author = Column(String(50))
    creation_time = Column(DateTime)
    note = Column(String(255))
    patient_id = Column(String(20), nullable=False)
    visit_id = Column(String(20), nullable=False)
    oper_id = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    record_id = Column(String(36))
    picture_id = Column(String(36))
    extend1 = Column(String(50))
    extend2 = Column(String(50))


class MedOronlineUser(Base):
    __tablename__ = 'med_oronline_users'

    online_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    user_id = Column(String(36))
    room_no = Column(String(20))
    dept_code = Column(String(20))
    online_type = Column(String(20))
    login_time = Column(DateTime)
    observe_id = Column(String(36))
    description = Column(String(100))


class MedPerioperativeEventConfig(Base):
    __tablename__ = 'med_perioperative_event_config'

    event_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    serial_no = Column(Numeric(3, 0, asdecimal=False))
    event_name = Column(String(50))
    event_period = Column(String(50))
    event_class = Column(String(50), server_default=text("'0'"))
    data_source = Column(String(100))
    data_source_type = Column(String(20), server_default=text("'T'"))
    data_key = Column(String(120))
    dll_function = Column(String(50))
    dll_function_params = Column(String(200))
    exe_function = Column(String(150))
    webpage_function = Column(String(150))
    data_select = Column(String(200))
    data_ind = Column(String(200))
    event_stutas = Column(String(2), server_default=text("'1'"))
    display_order = Column(Numeric(3, 0, asdecimal=False))
    priority = Column(String(5))
    warning_prompt = Column(String(50))
    memo = Column(String(100))
    event_category = Column(String(36))
    index_label_format = Column(String(80))
    event_time_field = Column(String(50))
    ifshowinclient = Column(String(1), server_default=text("'0'"))
    client_aliaes = Column(String(20))
    img_id = Column(String(36))
    isshowindexonmenu = Column(String(1), server_default=text("""\
'1'
"""))


class MedPerioperativeEventIndex(Base):
    __tablename__ = 'med_perioperative_event_index'

    index_id = Column(String(36), primary_key=True, server_default=text("sys_guid() "))
    patient_id = Column(String(20))
    visit_id = Column(String(20))
    oper_id = Column(Numeric(2, 0, asdecimal=False))
    event_id = Column(String(36))
    index_label = Column(String(50))
    event_time = Column(DateTime)
    data_key_val = Column(String(120))
    select_sql = Column(String(200))
    dll_function = Column(String(50))
    dll_function_paramvals = Column(String(200))
    exe_path = Column(String(150))
    webpage_url = Column(String(150))
    warning_prompt = Column(String(50))
    memo = Column(String(100))
    event_category = Column(String(36))


class MedUsersExt(Base):
    __tablename__ = 'med_users_ext'

    user_id = Column(String(36), primary_key=True)
    mcu_username = Column(String(50), nullable=False)
    mcu_userpwd = Column(String(50))
    memo = Column(String(100))
