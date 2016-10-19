# coding: utf-8
from sqlalchemy import Column, DateTime, Index, LargeBinary, Numeric, String, Table, text
from sqlalchemy.sql.sqltypes import NullType
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()
metadata = Base.metadata


class MedAdadminsterModeDict(Base):
    __tablename__ = 'med_adadminster_mode_dict'

    adadminster_no = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    adadminster_mode_code = Column(String(1), primary_key=True, nullable=False)
    adadminster_mode_name = Column(String(8))
    input_code = Column(String(8))


class MedAdministrationDict(Base):
    __tablename__ = 'med_administration_dict'

    serial_no = Column(Numeric(3, 0, asdecimal=False))
    administration_code = Column(String(3))
    administration_name = Column(String(30), primary_key=True)
    administration_abbr = Column(String(8))
    input_code = Column(String(16))


class MedAdministrationStatDict(Base):
    __tablename__ = 'med_administration_stat_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    item_name = Column(String(8), primary_key=True, nullable=False)
    administration = Column(String(30), primary_key=True, nullable=False)


class MedAdtLog(Base):
    __tablename__ = 'med_adt_log'

    ward_code = Column(String(16), primary_key=True, nullable=False)
    dept_code = Column(String(16), index=True)
    log_date_time = Column(DateTime, primary_key=True, nullable=False)
    patient_id = Column(String(20), primary_key=True, nullable=False, index=True)
    visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    action = Column(String(1), primary_key=True, nullable=False)


class MedAnaesthesiaDict(Base):
    __tablename__ = 'med_anaesthesia_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    anaesthesia_code = Column(String(1))
    anaesthesia_name = Column(String(40), primary_key=True)
    input_code = Column(String(8))
    anaesthesia_type = Column(String(16))
    anaesthesia_shorten = Column(String(40))
    need_anes_doctor = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))


class MedAnesthesiaItemClas(Base):
    __tablename__ = 'med_anesthesia_item_class'
    __table_args__ = (
        Index('ind_med_anesthesia_item_class', 'func', 'item_class', unique=True),
    )

    serial_no = Column(Numeric(4, 0, asdecimal=False), primary_key=True)
    func = Column(String(16), nullable=False)
    item_class = Column(String(40), nullable=False)
    item_code = Column(String(40))
    input_code = Column(String(8))


class MedAnestheticClassDict(Base):
    __tablename__ = 'med_anesthetic_class_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    class_name = Column(String(20), primary_key=True)
    input_code = Column(String(8))


class MedApplication(Base):
    __tablename__ = 'med_applications'

    app_id = Column(String(36), primary_key=True)
    name = Column(String(60), nullable=False, unique=True)
    description = Column(String(160))


class MedAreaDict(Base):
    __tablename__ = 'med_area_dict'

    serial_no = Column(Numeric(4, 0, asdecimal=False))
    area_code = Column(String(6), primary_key=True)
    area_name = Column(String(34))
    input_code = Column(String(8))
    zip_code = Column(String(6))


class MedBedRec(Base):
    __tablename__ = 'med_bed_rec'

    ward_code = Column(String(16), primary_key=True, nullable=False)
    bed_no = Column(String(20), primary_key=True, nullable=False)
    bed_label = Column(String(20))
    room_no = Column(String(20))
    dept_code = Column(String(16), index=True)
    bed_approved_type = Column(String(1))
    bed_sex_type = Column(String(1))
    bed_class = Column(String(2))
    bed_status = Column(String(1))
    icu_indicator = Column(Numeric(1, 0, asdecimal=False))
    monitor_label = Column(String(20))
    serial_no = Column(Numeric(3, 0, asdecimal=False))


class MedBillConfigDict(Base):
    __tablename__ = 'med_bill_config_dict'

    item_class = Column(String(16), primary_key=True, nullable=False)
    item_name = Column(String(60), primary_key=True, nullable=False)
    bill_mode = Column(String(20))
    bill_result_rule = Column(String(20))
    bill_time_rule = Column(String(20))
    bill_standard_time = Column(Numeric(5, 2))
    charge_item_class = Column(String(16))
    charge_item_code = Column(String(16))
    charge_item_name = Column(String(60))
    charge_item_spec = Column(String(20))
    units = Column(String(8))


class MedBillItemClassDict(Base):
    __tablename__ = 'med_bill_item_class_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    class_code = Column(String(16), primary_key=True)
    class_name = Column(String(60))
    input_code = Column(String(8))


class MedBillItemClassVsHi(Base):
    __tablename__ = 'med_bill_item_class_vs_his'

    class_code = Column(String(16), primary_key=True, nullable=False)
    code_in_his = Column(String(32), primary_key=True, nullable=False)


class MedBloodGasDetail(Base):
    __tablename__ = 'med_blood_gas_detail'

    detail_id = Column(String(30), primary_key=True, nullable=False)
    blg_code = Column(String(60), primary_key=True, nullable=False)
    blg_value = Column(String(20))
    operator = Column(String(20))
    op_date = Column(DateTime)
    abnormal_indicator = Column(String(2))


class MedBloodGasDict(Base):
    __tablename__ = 'med_blood_gas_dict'

    blg_code = Column(String(20), primary_key=True, nullable=False)
    blg_name = Column(String(60), nullable=False)
    blg_showid = Column(Numeric(asdecimal=False), primary_key=True, nullable=False)
    blg_unit = Column(String(20))
    blg_refer_value = Column(String(40))
    blg_status = Column(String(2), primary_key=True, nullable=False)
    blg_input_code = Column(String(20))
    blg_attr_code = Column(String(100))
    blg_item_id = Column(Numeric(4, 0, asdecimal=False))


class MedBloodGasMaster(Base):
    __tablename__ = 'med_blood_gas_master'

    patient_id = Column(String(20), nullable=False)
    visit_id = Column(Numeric(2, 0, asdecimal=False), nullable=False)
    record_date = Column(DateTime, nullable=False)
    nurse_memo1 = Column(String(600))
    nurse_memo2 = Column(String(600))
    detail_id = Column(String(30), primary_key=True)
    operator = Column(String(20))
    op_date = Column(DateTime)
    specimen = Column(String(100))
    equipment = Column(String(100))
    oper_id = Column(Numeric(2, 0, asdecimal=False))


class MedChargePriceSchedule(Base):
    __tablename__ = 'med_charge_price_schedule'

    charge_type = Column(String(8), primary_key=True)
    price_coeff_numerator = Column(Numeric(3, 0, asdecimal=False))
    price_coeff_denominator = Column(Numeric(3, 0, asdecimal=False))
    charge_special_indicator = Column(Numeric(1, 0, asdecimal=False))


class MedChargeTypeDict(Base):
    __tablename__ = 'med_charge_type_dict'

    serial_no = Column(Numeric(3, 0, asdecimal=False))
    charge_type_code = Column(String(2))
    charge_type_name = Column(String(30), primary_key=True)
    charge_price_indicator = Column(Numeric(1, 0, asdecimal=False))
    input_code = Column(String(16))


class MedClinicItemNameDict(Base):
    __tablename__ = 'med_clinic_item_name_dict'
    __table_args__ = (
        Index('ind_clinic_item_name_dict_1', 'item_class', 'item_code'),
    )

    item_class = Column(String(16), primary_key=True, nullable=False)
    item_name = Column(String(60), primary_key=True, nullable=False, index=True)
    item_code = Column(String(10))
    std_indicator = Column(Numeric(1, 0, asdecimal=False))
    input_code = Column(String(8))
    input_code_wb = Column(String(8))
    expand1 = Column(String(8))
    expand2 = Column(String(8))
    expand3 = Column(String(8))
    expand4 = Column(String(8))
    expand5 = Column(String(8))


class MedClinicVsCharge(Base):
    __tablename__ = 'med_clinic_vs_charge'

    clinic_item_class = Column(String(1), primary_key=True, nullable=False)
    clinic_item_code = Column(String(10), primary_key=True, nullable=False)
    charge_item_no = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    charge_item_class = Column(String(16))
    charge_item_code = Column(String(10))
    charge_item_spec = Column(String(20))
    amount = Column(Numeric(4, 0, asdecimal=False))
    units = Column(String(12))


t_med_current_price_list = Table(
    'med_current_price_list', metadata,
    Column('item_class', String(16)),
    Column('item_code', String(10)),
    Column('item_name', String(60)),
    Column('item_spec', String(20)),
    Column('units', String(8)),
    Column('price', Numeric(9, 3)),
    Column('prefer_price', Numeric(9, 3)),
    Column('foreigner_price', Numeric(9, 3)),
    Column('performed_by', String(8)),
    Column('fee_type_mask', Numeric(1, 0, asdecimal=False)),
    Column('class_on_inp_rcpt', String(1)),
    Column('class_on_outp_rcpt', String(1)),
    Column('class_on_reckoning', String(10)),
    Column('subj_code', String(3)),
    Column('class_on_mr', String(4)),
    Column('memo', String(40)),
    Column('operator', String(8)),
    Column('enter_date', DateTime)
)


class MedDataTableCodeDict(Base):
    __tablename__ = 'med_data_table_code_dict'

    show_no = Column(Numeric(3, 0, asdecimal=False))
    table_code = Column(String(20), primary_key=True)
    table_value = Column(String(50))
    show_name = Column(String(100))


class MedDeptDict(Base):
    __tablename__ = 'med_dept_dict'

    serial_no = Column(Numeric(4, 0, asdecimal=False))
    dept_code = Column(String(30), primary_key=True)
    dept_name = Column(String(40))
    input_code = Column(String(40))
    dept_alias = Column(String(40))

    def to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}


class MedDeptEquipDict(Base):
    __tablename__ = 'med_dept_equip_dict'

    ward_code = Column(String(8), primary_key=True, nullable=False)
    item_name = Column(String(10), primary_key=True, nullable=False)
    memo = Column(String(40))


class MedDeptVsWard(Base):
    __tablename__ = 'med_dept_vs_ward'

    dept_code = Column(String(8), primary_key=True)
    ward_code = Column(String(8), index=True)


class MedDiagnosisDict(Base):
    __tablename__ = 'med_diagnosis_dict'

    diagnosis_code = Column(String(16), primary_key=True)
    diagnosis_name = Column(String(40))
    std_indicator = Column(Numeric(1, 0, asdecimal=False))
    approved_indicator = Column(Numeric(1, 0, asdecimal=False))
    create_date = Column(DateTime)
    input_code = Column(String(8))
    infect_indicator = Column(String(1))
    health_level = Column(String(2))
    input_code_wb = Column(String(8))
    disease_sort = Column(String(4))
    diag_indicator = Column(Numeric(1, 0, asdecimal=False))


class MedDosageUnitsDict(Base):
    __tablename__ = 'med_dosage_units_dict'

    serial_no = Column(Numeric(3, 0, asdecimal=False))
    dosage_units = Column(String(8), primary_key=True)
    base_units = Column(String(8))
    conversion_ratio = Column(Numeric(12, 6))
    input_code = Column(String(8))


class MedDrugClassDict(Base):
    __tablename__ = 'med_drug_class_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    class_name = Column(String(10), primary_key=True)
    input_code = Column(String(8))


class MedDrugDict(Base):
    __tablename__ = 'med_drug_dict'

    drug_code = Column(String(16), primary_key=True, nullable=False)
    drug_name = Column(String(60), nullable=False)
    drug_spec = Column(String(20), primary_key=True, nullable=False)
    units = Column(String(8))
    drug_form = Column(String(20))
    supplier_name = Column(String(60))
    dose_per_unit = Column(Numeric(8, 3))
    dose_units = Column(String(8))
    drug_class = Column(String(10))
    anesthetic_class = Column(String(20))
    code_in_his = Column(String(16))
    input_code = Column(String(8))


class MedDrugFormDict(Base):
    __tablename__ = 'med_drug_form_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    form_name = Column(String(20), primary_key=True)
    input_code = Column(String(8))


class MedDrugNameDict(Base):
    __tablename__ = 'med_drug_name_dict'

    drug_code = Column(String(16), primary_key=True, nullable=False)
    drug_name = Column(String(60), primary_key=True, nullable=False)
    std_indicator = Column(Numeric(1, 0, asdecimal=False))
    input_code = Column(String(8))


class MedDrugReturnClassDict(Base):
    __tablename__ = 'med_drug_return_class_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    return_class = Column(String(8), primary_key=True)


class MedEmrArchiveDetial(Base):
    __tablename__ = 'med_emr_archive_detial'

    patient_id = Column(String(20), primary_key=True, nullable=False)
    visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    mr_class = Column(String(10), primary_key=True, nullable=False)
    mr_sub_class = Column(String(100), primary_key=True, nullable=False)
    archive_key = Column(String(20), primary_key=True, nullable=False)
    emr_file_index = Column(Numeric(3, 0, asdecimal=False), primary_key=True, nullable=False, server_default=text("0 "))
    archive_times = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    topic = Column(String(40))
    emr_file_name = Column(String(256))
    emr_type = Column(String(10))
    archive_date_time = Column(DateTime)
    archive_type = Column(String(10))
    archive_status = Column(String(10))
    emr_owner = Column(String(16))
    operator = Column(String(16))
    archive_pc = Column(String(80))
    archive_mode = Column(String(10))
    archive_access = Column(String(256))
    memo = Column(String(100))


class MedEmrClassDict(Base):
    __tablename__ = 'med_emr_class_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    mr_class = Column(String(10), primary_key=True, nullable=False)
    mr_sub_class = Column(String(10), primary_key=True, nullable=False)
    hide_indicator = Column(Numeric(1, 0, asdecimal=False))


class MedEmrUser(Base):
    __tablename__ = 'med_emr_users'

    user_id = Column(String(36), primary_key=True)
    login_name = Column(String(36))
    login_pwd = Column(String(36))
    name = Column(String(36))
    dept_code = Column(String(16))
    input_code = Column(String(8))
    job = Column(String(16))
    title = Column(String(10))
    grant_code = Column(String(20))
    is_valid = Column(Numeric(1, 0, asdecimal=False))


class MedEmrWorkPath(Base):
    __tablename__ = 'med_emr_work_path'

    application = Column(String(20), primary_key=True, nullable=False)
    emr_path = Column(String(240), primary_key=True, nullable=False)
    user_name = Column(String(16))
    user_pwd = Column(String(16))
    ip_addr = Column(String(64))


class MedExamItem(Base):
    __tablename__ = 'med_exam_items'

    exam_no = Column(String(20), primary_key=True, nullable=False)
    exam_item_no = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    exam_item = Column(String(80))
    exam_item_code = Column(String(10))
    costs = Column(Numeric(8, 2))


class MedExamMaster(Base):
    __tablename__ = 'med_exam_master'
    __table_args__ = (
        Index('ind_1_exam_master', 'patient_id', 'visit_id', 'exam_no'),
    )

    exam_no = Column(String(20), primary_key=True)
    local_id_class = Column(String(1))
    patient_local_id = Column(String(20))
    patient_id = Column(String(20))
    visit_id = Column(Numeric(2, 0, asdecimal=False))
    name = Column(String(30))
    sex = Column(String(4))
    date_of_birth = Column(DateTime)
    exam_class = Column(String(6))
    exam_sub_class = Column(String(8))
    spm_recved_date = Column(DateTime)
    clin_symp = Column(String(400))
    phys_sign = Column(String(400))
    relevant_lab_test = Column(String(200))
    relevant_diag = Column(String(400))
    clin_diag = Column(String(80))
    exam_mode = Column(String(1))
    exam_group = Column(String(16))
    device = Column(String(20))
    performed_by = Column(String(16))
    patient_source = Column(String(1))
    facility = Column(String(20))
    req_date_time = Column(DateTime)
    req_dept = Column(String(16))
    req_physician = Column(String(30))
    req_memo = Column(String(60))
    scheduled_date_time = Column(DateTime)
    notice = Column(String(400))
    exam_date_time = Column(DateTime, index=True)
    report_date_time = Column(DateTime)
    technician = Column(String(30))
    reporter = Column(String(30))
    result_status = Column(String(1))
    verified_by = Column(String(30))
    verified_date_time = Column(DateTime)


class MedExamReport(Base):
    __tablename__ = 'med_exam_report'

    exam_no = Column(String(20), primary_key=True)
    exam_para = Column(String(1000))
    description = Column(String(2000))
    impression = Column(String(2000))
    recommendation = Column(String(1000))
    is_abnormal = Column(String(1))
    use_image = Column(String(15))
    study_uid = Column(String(128))
    memo = Column(String(40))


class MedHisUser(Base):
    __tablename__ = 'med_his_users'

    user_id = Column(String(36), primary_key=True)
    user_name = Column(String(30), nullable=False)
    user_dept = Column(String(16))
    input_code = Column(String(8))
    user_job = Column(String(20))
    reserved01 = Column(String(50))
    create_date = Column(DateTime)
    operator_no = Column(String(36))


class MedHisUsersInfo(Base):
    __tablename__ = 'med_his_users_info'

    user_id = Column(String(36), primary_key=True)
    professional_title = Column(String(20))
    signature = Column(LargeBinary)
    memo = Column(String(100))


class MedHospitalConfig(Base):
    __tablename__ = 'med_hospital_config'

    hospital_id = Column(String(40), primary_key=True)
    hospital_name = Column(String(80))
    authorized_key = Column(String(20))
    unit_code = Column(String(11))
    location = Column(String(6))
    mailing_address = Column(String(80))
    zip_code = Column(String(6))
    approved_bed_num = Column(Numeric(4, 0, asdecimal=False))
    verify_key = Column(String(10))
    hospital_type = Column(Numeric(1, 0, asdecimal=False))
    hospital_class = Column(String(16))


class MedIcuConfig(Base):
    __tablename__ = 'med_icu_config'

    config_id = Column(String(20), primary_key=True)
    auditing_condition = Column(String(4000))
    dept = Column(String(4000))
    orders_in_mount = Column(String(4000))
    special_care = Column(String(4000))


class MedIcuShowDict(Base):
    __tablename__ = 'med_icu_show_dict'

    show_no = Column(Numeric(3, 0, asdecimal=False))
    show_code = Column(String(10), primary_key=True)
    show_name = Column(String(30))
    show_item_no = Column(Numeric(2, 0, asdecimal=False))
    show_state = Column(Numeric(2, 0, asdecimal=False))


class MedIcuShowSubDict(Base):
    __tablename__ = 'med_icu_show_sub_dict'

    show_sub_no = Column(Numeric(3, 0, asdecimal=False))
    show_code = Column(String(10))
    show_sub_code = Column(String(10), primary_key=True)
    show_sub_name = Column(String(30))
    in_or_out = Column(Numeric(1, 0, asdecimal=False))
    show_sub_item_no = Column(Numeric(4, 0, asdecimal=False))


class MedIcuValueTypeDict(Base):
    __tablename__ = 'med_icu_value_type_dict'

    show_no = Column(Numeric(3, 0, asdecimal=False))
    value_type = Column(Numeric(1, 0, asdecimal=False), primary_key=True)
    value_name = Column(String(20))
    value_memo = Column(String(100))


class MedIdentityDict(Base):
    __tablename__ = 'med_identity_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    identity_code = Column(String(1))
    identity_name = Column(String(10), primary_key=True)
    input_code = Column(String(8))
    priority_indicator = Column(Numeric(1, 0, asdecimal=False))
    military_indicator = Column(Numeric(1, 0, asdecimal=False))
    charge_type = Column(String(1))
    input_code_wb = Column(String(8))


class MedIfHisViewSql(Base):
    __tablename__ = 'med_if_his_view_sql'

    serial_no = Column(Numeric(3, 0, asdecimal=False))
    sql_text = Column(String(2000))
    his_table_name = Column(String(40))
    med_table_name = Column(String(40), primary_key=True, nullable=False)
    para_code = Column(String(100))
    description = Column(String(100))
    sql_type = Column(String(20))
    dbms_type = Column(String(20), primary_key=True, nullable=False)
    command_type = Column(String(20))


t_med_if_log = Table(
    'med_if_log', metadata,
    Column('id', String(40)),
    Column('ldate', String(20)),
    Column('ltime', String(20)),
    Column('title', String(200)),
    Column('module', String(100)),
    Column('grade', String(30)),
    Column('content', String(2000)),
    Column('source', String(20)),
    Column('category', String(20)),
    Column('isshow', String(1)),
    Column('currentuser', String(200))
)


class MedIfRunConfigDict(Base):
    __tablename__ = 'med_if_run_config_dict'

    app_class = Column(String(16), primary_key=True, nullable=False)
    section = Column(String(20), primary_key=True, nullable=False)
    main_key = Column(String(20), primary_key=True, nullable=False)
    key_value = Column(String(100))
    memo = Column(String(500))


class MedIfTransDict(Base):
    __tablename__ = 'med_if_trans_dict'

    trans_name = Column(String(20), primary_key=True)
    dbms = Column(String(40), nullable=False)
    server_name = Column(String(30))
    database = Column(String(20))
    log_id = Column(String(20), nullable=False)
    log_pass = Column(String(20), nullable=False)
    nls_lang = Column(String(40))
    dbparm = Column(String(80))
    memo = Column(String(80))


class MedInputorderTemplete(Base):
    __tablename__ = 'med_inputorder_templete'

    ward_code = Column(String(8), primary_key=True, nullable=False)
    templete_code = Column(String(10))
    templete_name = Column(String(40), primary_key=True, nullable=False)
    templete_desc = Column(String(1000))
    input_code = Column(String(8))


class MedJobClassDict(Base):
    __tablename__ = 'med_job_class_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    job_class_code = Column(String(2))
    job_class_name = Column(String(8), primary_key=True)
    input_code = Column(String(8))


class MedLabReportItemDict(Base):
    __tablename__ = 'med_lab_report_item_dict'

    serial_no = Column(Numeric(4, 0, asdecimal=False))
    item_code = Column(String(10), primary_key=True)
    item_name = Column(String(40))
    result_type = Column(String(8))
    lower_limit = Column(Numeric(9, 3))
    upper_limit = Column(Numeric(9, 3))
    units = Column(String(8))
    print_context = Column(String(80))
    mini_increment = Column(Numeric(6, 3))
    notes = Column(String(40))
    default_value = Column(String(20))
    input_code = Column(String(8))


class MedLabResult(Base):
    __tablename__ = 'med_lab_result'

    test_no = Column(String(20), primary_key=True, nullable=False)
    item_no = Column(Numeric(10, 0, asdecimal=False), primary_key=True, nullable=False)
    print_order = Column(Numeric(4, 0, asdecimal=False), primary_key=True, nullable=False)
    report_item_name = Column(String(80))
    report_item_code = Column(String(10))
    result = Column(String(80))
    units = Column(String(20))
    abnormal_indicator = Column(String(1))
    instrument_id = Column(String(8))
    result_date_time = Column(DateTime)
    reference_result = Column(String(200))


class MedLabTestItem(Base):
    __tablename__ = 'med_lab_test_items'

    test_no = Column(String(20), primary_key=True, nullable=False)
    item_no = Column(Numeric(10, 0, asdecimal=False), primary_key=True, nullable=False)
    item_name = Column(String(80))
    item_code = Column(String(10))


class MedLabTestMaster(Base):
    __tablename__ = 'med_lab_test_master'

    test_no = Column(String(20), primary_key=True)
    priority_indicator = Column(Numeric(1, 0, asdecimal=False))
    patient_id = Column(String(20), index=True)
    visit_id = Column(Numeric(2, 0, asdecimal=False))
    working_id = Column(String(20))
    execute_date = Column(DateTime)
    name = Column(String(30))
    name_phonetic = Column(String(16))
    charge_type = Column(String(30))
    sex = Column(String(4))
    age = Column(Numeric(3, 0, asdecimal=False))
    test_cause = Column(String(500))
    relevant_clinic_diag = Column(String(200))
    specimen = Column(String(100))
    notes_for_spcm = Column(String(16))
    spcm_received_date_time = Column(DateTime)
    spcm_sample_date_time = Column(DateTime)
    requested_date_time = Column(DateTime)
    ordering_dept = Column(String(16))
    ordering_provider = Column(String(30))
    performed_by = Column(String(16))
    result_status = Column(String(1))
    results_rpt_date_time = Column(DateTime)
    transcriptionist = Column(String(30))
    verified_by = Column(String(8))
    costs = Column(Numeric(8, 2))
    charges = Column(Numeric(8, 2))
    billing_indicator = Column(Numeric(1, 0, asdecimal=False))
    print_indicator = Column(Numeric(1, 0, asdecimal=False))
    subject = Column(String(40))
    barcode = Column(String(10))


class MedMaritalStatusDict(Base):
    __tablename__ = 'med_marital_status_dict'

    serial_no = Column(Numeric(1, 0, asdecimal=False))
    marital_status_code = Column(String(1))
    marital_status_name = Column(String(4), primary_key=True)
    input_code = Column(String(8))


class MedMeasuresDict(Base):
    __tablename__ = 'med_measures_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    measures_class = Column(String(10), primary_key=True, nullable=False)
    measures_code = Column(String(3))
    measures_name = Column(String(8), primary_key=True, nullable=False)
    base_units = Column(String(8))
    conversion_ratio = Column(Numeric(12, 6))
    input_code = Column(String(8))


class MedMonitorDataValuesDict(Base):
    __tablename__ = 'med_monitor_data_values_dict'

    monitor_data_name = Column(String(40), primary_key=True, nullable=False)
    monitor_data_alias = Column(String(8))
    monitor_data_value = Column(String(40), primary_key=True, nullable=False)
    print_value = Column(String(40))
    input_code = Column(String(8))
    content_id = Column(String(2))


class MedMonitorDict(Base):
    __tablename__ = 'med_monitor_dict'

    monitor_label = Column(String(20), primary_key=True)
    manu_firm_name = Column(String(40))
    model = Column(String(40))
    interface_type = Column(Numeric(1, 0, asdecimal=False))
    interface_desc = Column(String(20))
    ip_addr = Column(String(15))
    mac_addr = Column(String(12))
    last_recv_time = Column(DateTime)
    last_recv_bed_id = Column(String(5))
    duplex_flag = Column(Numeric(5, 0, asdecimal=False))
    autoin_flag = Column(String(1))
    comm_port = Column(String(6))
    baud_rate = Column(Numeric(5, 0, asdecimal=False))
    byte_size = Column(Numeric(5, 0, asdecimal=False))
    parity = Column(Numeric(5, 0, asdecimal=False))
    stop_bits = Column(Numeric(5, 0, asdecimal=False))
    f_outx = Column(Numeric(5, 0, asdecimal=False))
    f_inx = Column(Numeric(5, 0, asdecimal=False))
    f_hardware = Column(Numeric(5, 0, asdecimal=False))
    tx_queuesize = Column(Numeric(5, 0, asdecimal=False))
    rx_queuesize = Column(Numeric(5, 0, asdecimal=False))
    xon_lim = Column(Numeric(5, 0, asdecimal=False))
    xoff_lim = Column(Numeric(5, 0, asdecimal=False))
    xon_char = Column(String(1))
    xoff_char = Column(String(1))
    error_char = Column(String(1))
    event_char = Column(String(1))
    driver_prog = Column(String(128))
    priority = Column(Numeric(5, 0, asdecimal=False))
    item_type = Column(String(1))
    auto_load = Column(Numeric(5, 0, asdecimal=False))
    start_date_time = Column(DateTime)
    default_recv_frequency = Column(Numeric(5, 0, asdecimal=False))
    current_recv_frequency = Column(Numeric(5, 0, asdecimal=False))
    current_recvtimes_uplimit = Column(Numeric(5, 0, asdecimal=False))
    current_recv_items = Column(String(200))
    ward_code = Column(String(8))
    ward_type = Column(Numeric(2, 0, asdecimal=False))
    bed_no = Column(String(20))
    patient_id = Column(String(20))
    visit_id = Column(Numeric(2, 0, asdecimal=False))
    oper_id = Column(Numeric(2, 0, asdecimal=False))
    using_indicator = Column(Numeric(1, 0, asdecimal=False))
    frequency_display = Column(Numeric(5, 0, asdecimal=False))
    memo = Column(String(100))
    datalog_start_time = Column(DateTime)
    pc_port = Column(Numeric(5, 0, asdecimal=False))
    datalog_status = Column(String(4))
    ip_port = Column(Numeric(5, 0, asdecimal=False))
    in_port = Column(Numeric(5, 0, asdecimal=False))
    out_port = Column(Numeric(5, 0, asdecimal=False))


class MedMonitorFunctionCode(Base):
    __tablename__ = 'med_monitor_function_code'

    item_id = Column(Numeric(5, 0, asdecimal=False))
    item_name = Column(String(40))
    item_code = Column(String(6), primary_key=True)
    item_unit = Column(String(8))
    dis_color = Column(Numeric(8, 0, asdecimal=False))
    parm_class = Column(String(1))
    draw_icon = Column(String(2))
    use_flag = Column(String(1))
    priority_indi = Column(Numeric(1, 0, asdecimal=False))
    memo = Column(String(24))
    input_code = Column(String(8))
    name_in_icu = Column(String(16))
    ward_code = Column(String(8))
    ward_type = Column(Numeric(2, 0, asdecimal=False))
    item_name_alias = Column(String(8))
    value_type = Column(Numeric(1, 0, asdecimal=False))
    exam_method = Column(Numeric(1, 0, asdecimal=False))
    in_or_out = Column(Numeric(1, 0, asdecimal=False))
    item_type = Column(Numeric(1, 0, asdecimal=False))
    calc_sum = Column(Numeric(1, 0, asdecimal=False))
    print_item_no = Column(Numeric(2, 0, asdecimal=False))
    draw_style = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))
    draw_isvalid = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))
    show_sub_code = Column(String(10))
    data_table_code = Column(String(100))


class MedMonitorSpecialCode(Base):
    __tablename__ = 'med_monitor_special_code'

    item_id = Column(Numeric(5, 0, asdecimal=False))
    item_name = Column(String(40))
    item_code = Column(String(6), primary_key=True)
    item_unit = Column(String(8))
    dis_color = Column(Numeric(8, 0, asdecimal=False))
    parm_class = Column(String(1))
    draw_icon = Column(String(2))
    use_flag = Column(String(1))
    priority_indi = Column(Numeric(1, 0, asdecimal=False))
    memo = Column(String(24))
    input_code = Column(String(8))
    name_in_icu = Column(String(16))
    ward_code = Column(String(8))
    ward_type = Column(Numeric(2, 0, asdecimal=False))
    item_name_alias = Column(String(8))
    value_type = Column(Numeric(1, 0, asdecimal=False))
    exam_method = Column(Numeric(1, 0, asdecimal=False))
    in_or_out = Column(Numeric(1, 0, asdecimal=False))
    item_type = Column(Numeric(1, 0, asdecimal=False))
    calc_sum = Column(Numeric(1, 0, asdecimal=False))
    print_item_no = Column(Numeric(2, 0, asdecimal=False))
    draw_style = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))
    draw_isvalid = Column(Numeric(1, 0, asdecimal=False), server_default=text("1"))
    show_sub_code = Column(String(10))
    data_table_code = Column(String(100))


class MedMrContent(Base):
    __tablename__ = 'med_mr_content'

    patient_id = Column(String(20), primary_key=True, nullable=False)
    visit_id = Column(String(2), primary_key=True, nullable=False)
    file_no = Column(String(2), primary_key=True, nullable=False)
    mr_cont = Column(NullType)


class MedMrFile(Base):
    __tablename__ = 'med_mr_file'

    patient_id = Column(String(20), primary_key=True, nullable=False)
    visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    file_no = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    topic = Column(String(40))
    creator_id = Column(String(16))
    create_date_time = Column(DateTime)
    templet_id = Column(String(6))
    mr_modify_times = Column(Numeric(3, 0, asdecimal=False))
    mr_print_times = Column(Numeric(3, 0, asdecimal=False))
    current_user_name = Column(String(8))
    capability = Column(String(1))
    checkup_mark = Column(String(1))
    returned_mark = Column(String(1))
    last_modidate = Column(DateTime)


class MedMrFileIndex(Base):
    __tablename__ = 'med_mr_file_index'

    patient_id = Column(String(20), primary_key=True, nullable=False)
    visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    file_no = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    file_name = Column(String(16))
    topic = Column(String(40))
    creator_name = Column(String(30))
    creator_id = Column(String(16))
    create_date_time = Column(DateTime)
    last_modify_date_time = Column(DateTime)
    file_flag = Column(String(4))
    file_attr = Column(String(4))


class MedMrIndex(Base):
    __tablename__ = 'med_mr_index'

    patient_id = Column(String(20), primary_key=True, nullable=False)
    visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    mr_status = Column(String(1))
    storage_volume_label = Column(String(32))
    access_path = Column(String(40))
    last_access_date_time = Column(DateTime)


class MedMrWorkPath(Base):
    __tablename__ = 'med_mr_work_path'

    mr_path = Column(String(40), primary_key=True)
    templet_path = Column(String(40))
    file_user = Column(String(16))
    file_pwd = Column(String(16))
    ip_addr = Column(String(64))


class MedMtrlClassDict(Base):
    __tablename__ = 'med_mtrl_class_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    class_name = Column(String(10), primary_key=True)
    input_code = Column(String(8))


class MedMtrlDict(Base):
    __tablename__ = 'med_mtrl_dict'

    mtrl_code = Column(String(16), primary_key=True, nullable=False)
    mtrl_name = Column(String(60), nullable=False)
    mtrl_spec = Column(String(20), primary_key=True, nullable=False)
    units = Column(String(8))
    mtrl_class = Column(String(10))
    code_in_his = Column(String(16))
    input_code = Column(String(8))


class MedMtrlExportClassDict(Base):
    __tablename__ = 'med_mtrl_export_class_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    export_class = Column(String(8), primary_key=True)


class MedMtrlImportClassDict(Base):
    __tablename__ = 'med_mtrl_import_class_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    import_class = Column(String(8), primary_key=True)


class MedMtrlNameDict(Base):
    __tablename__ = 'med_mtrl_name_dict'

    mtrl_code = Column(String(16), primary_key=True, nullable=False)
    mtrl_name = Column(String(60), primary_key=True, nullable=False)
    std_indicator = Column(Numeric(1, 0, asdecimal=False))
    input_code = Column(String(8))


class MedMtrlSupplierCatalog(Base):
    __tablename__ = 'med_mtrl_supplier_catalog'

    supplier_id = Column(String(16), primary_key=True)
    supplier = Column(String(60), nullable=False)
    supplier_class = Column(String(8))
    code_in_his = Column(String(16))
    input_code = Column(String(8))


class MedNurseTemplete(Base):
    __tablename__ = 'med_nurse_templete'

    ward_code = Column(String(8), primary_key=True, nullable=False)
    templete_code = Column(String(10))
    templete_name = Column(String(40), primary_key=True, nullable=False)
    templete_desc = Column(String(1000))
    input_code = Column(String(8))


class MedNursingClassDict(Base):
    __tablename__ = 'med_nursing_class_dict'

    serial_no = Column(Numeric(1, 0, asdecimal=False))
    nursing_class_code = Column(String(1), primary_key=True)
    nursing_class_name = Column(String(8))
    input_code = Column(String(8))


class MedNursingScheduleDict(Base):
    __tablename__ = 'med_nursing_schedule_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    ward_code = Column(String(8), primary_key=True, nullable=False)
    schedule_name = Column(String(8), primary_key=True, nullable=False)
    start_time = Column(String(5))
    end_time = Column(String(5))


class MedOccupationDict(Base):
    __tablename__ = 'med_occupation_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    occupation_code = Column(String(1), primary_key=True)
    occupation_name = Column(String(20))
    input_code = Column(String(8))


class MedOperRoomUser(Base):
    __tablename__ = 'med_oper_room_users'

    user_id = Column(String(36), primary_key=True)
    user_name = Column(String(30))
    user_dept = Column(String(16))
    user_job = Column(String(8))
    status = Column(Numeric(1, 0, asdecimal=False))
    create_date = Column(DateTime)
    reserved01 = Column(String(50))
    input_code = Column(String(30))
    status_now = Column(Numeric(1, 0, asdecimal=False))


class MedOperationDict(Base):
    __tablename__ = 'med_operation_dict'

    operation_code = Column(String(16), index=True)
    operation_name = Column(String(60), primary_key=True)
    operation_scale = Column(String(2))
    std_indicator = Column(Numeric(1, 0, asdecimal=False))
    approved_indicator = Column(Numeric(1, 0, asdecimal=False))
    create_date = Column(DateTime)
    input_code = Column(String(8))
    input_code_wb = Column(String(8))


class MedOperationScaleDict(Base):
    __tablename__ = 'med_operation_scale_dict'

    serial_no = Column(Numeric(1, 0, asdecimal=False))
    operation_scale_code = Column(String(1), primary_key=True)
    operation_scale_name = Column(String(2))
    input_code = Column(String(8))


class MedOperroomCupboard(Base):
    __tablename__ = 'med_operroom_cupboard'

    cupboard = Column(String(3), primary_key=True)
    memo = Column(String(100))
    status = Column(Numeric(1, 0, asdecimal=False))


class MedOrderAttrDict(Base):
    __tablename__ = 'med_order_attr_dict'

    vital_signs = Column(String(100), primary_key=True)
    order_attr = Column(String(8))
    unit_weight_mount = Column(String(20))


class MedOrderClassDict(Base):
    __tablename__ = 'med_order_class_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    order_class_code = Column(String(1), primary_key=True)
    order_class_name = Column(String(8))
    input_code = Column(String(8))


class MedOrderStatusDict(Base):
    __tablename__ = 'med_order_status_dict'

    serial_no = Column(Numeric(1, 0, asdecimal=False))
    order_status_code = Column(String(1), primary_key=True)
    order_status_name = Column(String(8))
    input_code = Column(String(8))


class MedOrder(Base):
    __tablename__ = 'med_orders'

    patient_id = Column(String(20), primary_key=True, nullable=False)
    visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    order_no = Column(String(20), primary_key=True, nullable=False)
    order_sub_no = Column(Numeric(20, 0, asdecimal=False), primary_key=True, nullable=False)
    repeat_indicator = Column(Numeric(1, 0, asdecimal=False))
    order_class = Column(String(1))
    order_text = Column(String(200))
    order_code = Column(String(20))
    dosage = Column(Numeric(14, 4))
    dosage_units = Column(String(8))
    administration = Column(String(30))
    start_date_time = Column(DateTime)
    stop_date_time = Column(DateTime)
    duration = Column(Numeric(8, 0, asdecimal=False))
    duration_units = Column(String(8))
    frequency = Column(String(30))
    freq_counter = Column(Numeric(8, 0, asdecimal=False))
    freq_interval = Column(Numeric(8, 0, asdecimal=False))
    freq_interval_unit = Column(String(8))
    freq_detail = Column(String(30))
    perform_schedule = Column(String(60))
    perform_result = Column(String(20))
    ordering_dept = Column(String(16))
    doctor = Column(String(30))
    stop_doctor = Column(String(30))
    nurse = Column(String(30))
    stop_nurse = Column(String(30))
    enter_date_time = Column(DateTime)
    stop_order_date_time = Column(DateTime)
    order_status = Column(String(1))
    billing_attr = Column(Numeric(1, 0, asdecimal=False))
    last_perform_date_time = Column(DateTime)
    last_accting_date_time = Column(DateTime)
    drug_billing_attr = Column(Numeric(1, 0, asdecimal=False))
    treat_sheet_flag = Column(String(1))
    pham_std_code = Column(String(14))
    amount = Column(Numeric(3, 0, asdecimal=False))
    reserved1 = Column(String(10))
    dispense_memos = Column(String(20))
    current_presc_no = Column(Numeric(6, 0, asdecimal=False))
    drug_spec = Column(String(40))
    qty = Column(Numeric(10, 2))
    oper_order_flag = Column(String(1))


class MedOuterAppUse(Base):
    __tablename__ = 'med_outer_app_use'

    application = Column(String(16), primary_key=True, nullable=False)
    dict_file_name = Column(String(16), primary_key=True, nullable=False)


class MedOuterCodingConfig(Base):
    __tablename__ = 'med_outer_coding_config'

    topic = Column(String(8), primary_key=True, nullable=False)
    item_class = Column(String(4))
    coding_schm = Column(String(4), primary_key=True, nullable=False)
    outer_code_length = Column(Numeric(2, 0, asdecimal=False))
    text_length = Column(Numeric(3, 0, asdecimal=False))
    std_code_length = Column(Numeric(2, 0, asdecimal=False))
    dict_file_name = Column(String(16))
    last_updt_date_time = Column(DateTime)


class MedOuterGeneration(Base):
    __tablename__ = 'med_outer_generation'

    dict_file_name = Column(String(16), primary_key=True)
    data_table_name = Column(String(32), nullable=False)
    data_input_field = Column(String(32), nullable=False)
    data_code_field = Column(String(32), nullable=False)
    data_name_field = Column(String(32), nullable=False)
    data_filter = Column(String(128))
    updt_method = Column(Numeric(3, 0, asdecimal=False))
    dict_txt_file = Column(NullType)
    input_code_wb = Column(String(32))


class MedPatMasterIndex(Base):
    __tablename__ = 'med_pat_master_index'

    patient_id = Column(String(20), primary_key=True)
    inp_no = Column(String(20), index=True)
    name = Column(String(30), index=True)
    name_phonetic = Column(String(16), index=True)
    sex = Column(String(4))
    date_of_birth = Column(DateTime)
    birth_place = Column(String(60))
    citizenship = Column(String(30))
    nation = Column(String(30))
    id_no = Column(String(20))
    identity = Column(String(10))
    charge_type = Column(String(30))
    unit_in_contract = Column(String(11))
    mailing_address = Column(String(80))
    zip_code = Column(String(6))
    phone_number_home = Column(String(40))
    phone_number_business = Column(String(40))
    next_of_kin = Column(String(30))
    relationship = Column(String(20))
    next_of_kin_addr = Column(String(80))
    next_of_kin_zip_code = Column(String(6))
    next_of_kin_phone = Column(String(40))
    last_visit_date = Column(DateTime)
    vip_indicator = Column(Numeric(1, 0, asdecimal=False))
    create_date = Column(DateTime)
    operator = Column(String(30))


class MedPatMonitorDataDict(Base):
    __tablename__ = 'med_pat_monitor_data_dict'

    patient_id = Column(String(20), primary_key=True, nullable=False)
    visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    dep_id = Column(Numeric(2, 0, asdecimal=False))
    monitor_data_name = Column(String(40))
    db_data_name = Column(String(40), primary_key=True, nullable=False)
    low_signs_values = Column(Numeric(6, 2))
    high_signs_values = Column(Numeric(6, 2))


class MedPatVisit(Base):
    __tablename__ = 'med_pat_visit'

    patient_id = Column(String(20), primary_key=True, nullable=False)
    visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    dept_admission_to = Column(String(16), index=True)
    admission_date_time = Column(DateTime, index=True)
    dept_discharge_from = Column(String(16))
    discharge_date_time = Column(DateTime, index=True)
    occupation = Column(String(1))
    marital_status = Column(String(4))
    identity = Column(String(10))
    armed_services = Column(String(4))
    duty = Column(String(4))
    top_unit = Column(String(1))
    service_system_indicator = Column(Numeric(1, 0, asdecimal=False))
    unit_in_contract = Column(String(11))
    charge_type = Column(String(30))
    working_status = Column(Numeric(1, 0, asdecimal=False))
    insurance_type = Column(String(16))
    insurance_no = Column(String(18))
    service_agency = Column(String(80))
    mailing_address = Column(String(80))
    zip_code = Column(String(6))
    next_of_kin = Column(String(30))
    relationship = Column(String(2))
    next_of_kin_addr = Column(String(80))
    next_of_kin_zipcode = Column(String(6))
    next_of_kin_phone = Column(String(40))
    patient_class = Column(String(1))
    admission_cause = Column(String(8))
    consulting_date = Column(DateTime)
    pat_adm_condition = Column(String(1))
    consulting_doctor = Column(String(30))
    admitted_by = Column(String(30))
    emer_treat_times = Column(Numeric(2, 0, asdecimal=False))
    esc_emer_times = Column(Numeric(2, 0, asdecimal=False))
    serious_cond_days = Column(Numeric(4, 0, asdecimal=False))
    critical_cond_days = Column(Numeric(4, 0, asdecimal=False))
    icu_days = Column(Numeric(4, 0, asdecimal=False))
    ccu_days = Column(Numeric(4, 0, asdecimal=False))
    spec_level_nurs_days = Column(Numeric(4, 0, asdecimal=False))
    first_level_nurs_days = Column(Numeric(4, 0, asdecimal=False))
    second_level_nurs_days = Column(Numeric(4, 0, asdecimal=False))
    autopsy_indicator = Column(Numeric(1, 0, asdecimal=False))
    blood_type = Column(String(2))
    blood_type_rh = Column(String(1))
    infusion_react_times = Column(Numeric(2, 0, asdecimal=False))
    blood_tran_times = Column(Numeric(2, 0, asdecimal=False))
    blood_tran_vol = Column(Numeric(5, 0, asdecimal=False))
    blood_tran_react_times = Column(Numeric(2, 0, asdecimal=False))
    decubital_ulcer_times = Column(Numeric(2, 0, asdecimal=False))
    alergy_drugs = Column(String(80))
    adverse_reaction_drugs = Column(String(80))
    mr_value = Column(String(4))
    mr_quality = Column(String(2))
    follow_indicator = Column(Numeric(1, 0, asdecimal=False))
    follow_interval = Column(Numeric(2, 0, asdecimal=False))
    follow_interval_units = Column(String(2))
    director = Column(String(30))
    attending_doctor = Column(String(30))
    doctor_in_charge = Column(String(30))
    discharge_disposition = Column(String(1))
    total_costs = Column(Numeric(10, 2))
    total_payments = Column(Numeric(10, 2))
    catalog_date = Column(DateTime)
    cataloger = Column(String(8))
    reserved01 = Column(String(50))
    reserved02 = Column(String(50))
    reserved03 = Column(String(50))
    reserved04 = Column(String(50))
    reserved05 = Column(String(50))
    reserved06 = Column(String(50))
    reserved07 = Column(String(50))
    reserved08 = Column(String(50))
    reserved09 = Column(String(50))
    reserved10 = Column(String(50))
    reserved_date01 = Column(DateTime)
    reserved_date02 = Column(DateTime)
    body_height = Column(Numeric(4, 1))
    body_weight = Column(Numeric(4, 1))
    patient_condition = Column(String(12))
    abnormal = Column(String(80))


t_med_patient_archive_info = Table(
    'med_patient_archive_info', metadata,
    Column('his_patient_id', String(20)),
    Column('his_inp_no', String(20)),
    Column('mr_class', String(10), nullable=False),
    Column('mr_sub_class', String(100), nullable=False),
    Column('topic', String(40)),
    Column('archive_key', String(20), nullable=False),
    Column('archive_times', Numeric(2, 0, asdecimal=False), nullable=False),
    Column('archive_access', String(753)),
    Column('ip_addr', String(64)),
    Column('archive_status', String(10))
)


class MedPatientFormDataDict(Base):
    __tablename__ = 'med_patient_form_data_dict'

    patient_id = Column(String(20), primary_key=True, nullable=False)
    visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    item_no = Column(Numeric(2, 0, asdecimal=False))
    item_name = Column(String(20), primary_key=True, nullable=False)
    item_unit = Column(String(10))


class MedPatientStatusChgDict(Base):
    __tablename__ = 'med_patient_status_chg_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    patient_status_chg_code = Column(String(4), primary_key=True)
    patient_status_chg_name = Column(String(10))
    input_code = Column(String(8))


class MedPatientStatusDict(Base):
    __tablename__ = 'med_patient_status_dict'

    serial_no = Column(Numeric(1, 0, asdecimal=False))
    patient_status_code = Column(String(1), primary_key=True)
    patient_status_name = Column(String(4))
    input_code = Column(String(8))


class MedPatsInHospital(Base):
    __tablename__ = 'med_pats_in_hospital'
    __table_args__ = (
        Index('ind_1_med_pats_in_hospital', 'ward_code', 'bed_no'),
    )

    patient_id = Column(String(20), primary_key=True, nullable=False)
    visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    dep_id = Column(Numeric(2, 0, asdecimal=False))
    ward_code = Column(String(16))
    dept_code = Column(String(16))
    bed_no = Column(String(20))
    admission_date_time = Column(DateTime)
    adm_ward_date_time = Column(DateTime)
    diagnosis = Column(String(200))
    patient_condition = Column(String(1))
    nursing_class = Column(String(1))
    doctor_in_charge = Column(String(30))
    operating_date = Column(DateTime)
    billing_date_time = Column(DateTime)
    prepayments = Column(Numeric(10, 2))
    total_costs = Column(Numeric(10, 2))
    total_charges = Column(Numeric(10, 2))
    guarantor = Column(String(8))
    guarantor_org = Column(String(40))
    guarantor_phone_num = Column(String(16))
    bill_checked_date_time = Column(DateTime)
    settled_indicator = Column(Numeric(1, 0, asdecimal=False))
    reserved01 = Column(String(50))
    reserved02 = Column(String(50))
    reserved03 = Column(String(50))
    reserved04 = Column(String(50))
    reserved05 = Column(String(50))
    reserved06 = Column(String(50))
    reserved07 = Column(String(50))
    reserved08 = Column(String(50))
    reserved09 = Column(String(50))
    reserved10 = Column(String(50))
    reserved_date01 = Column(DateTime)
    reserved_date02 = Column(DateTime)
    start_date_time = Column(DateTime)
    frequency_nurse = Column(Numeric(5, 0, asdecimal=False))
    nurse_in_charge = Column(String(30))


class MedPerformDefaultSchedule(Base):
    __tablename__ = 'med_perform_default_schedule'

    serial_no = Column(Numeric(3, 0, asdecimal=False))
    freq_desc = Column(String(16), primary_key=True, nullable=False)
    administration = Column(String(16), primary_key=True, nullable=False)
    default_schedule = Column(String(60))


class MedPermission(Base):
    __tablename__ = 'med_permissions'

    permission_id = Column(String(36), primary_key=True)
    app_id = Column(String(36), nullable=False)
    name = Column(String(100), nullable=False)
    permission_key = Column(String(160), nullable=False)
    sort_id = Column(Numeric(10, 0, asdecimal=False))
    is_valid = Column(String(1), nullable=False, server_default=text("'T' "))
    description = Column(String(160))


class MedPermissionsAne(Base):
    __tablename__ = 'med_permissions_anes'

    permission_id = Column(String(36), primary_key=True)
    type = Column(String(2))
    module = Column(String(6))
    pic = Column(String(50))
    wd_name = Column(String(2000))
    wd_desc = Column(String(60))
    wd_menuname = Column(String(2000))
    menu_key = Column(String(60))
    parent_id = Column(String(36))
    child_id = Column(String(36))


class MedPermissionsProvider(Base):
    __tablename__ = 'med_permissions_provider'

    permission_id = Column(String(36), primary_key=True)
    parent_permission_id = Column(String(36), nullable=False)
    app_id = Column(String(36), nullable=False)


class MedPriceItemNameDict(Base):
    __tablename__ = 'med_price_item_name_dict'

    item_class = Column(String(16), primary_key=True, nullable=False)
    item_name = Column(String(60), primary_key=True, nullable=False)
    item_code = Column(String(10))
    std_indicator = Column(Numeric(1, 0, asdecimal=False))
    input_code = Column(String(8))
    custom_code = Column(String(8))
    input_code_wb = Column(String(8))
    stop_flag = Column(String(2))


t_med_price_list = Table(
    'med_price_list', metadata,
    Column('item_class', String(16)),
    Column('item_code', String(10)),
    Column('item_name', String(60)),
    Column('item_spec', String(20)),
    Column('units', String(8)),
    Column('price', Numeric(9, 3)),
    Column('prefer_price', Numeric(9, 3)),
    Column('foreigner_price', Numeric(9, 3)),
    Column('performed_by', String(8)),
    Column('fee_type_mask', Numeric(1, 0, asdecimal=False)),
    Column('class_on_inp_rcpt', String(1)),
    Column('class_on_outp_rcpt', String(1)),
    Column('class_on_reckoning', String(10)),
    Column('subj_code', String(3)),
    Column('class_on_mr', String(4)),
    Column('memo', String(40)),
    Column('start_date', DateTime),
    Column('stop_date', DateTime),
    Column('operator', String(8)),
    Column('enter_date', DateTime),
    Column('input_code', String(8)),
    Column('reserved1', String(50)),
    Column('reserved2', String(50)),
    Column('reserved3', String(50)),
    Column('reserved4', Numeric(3, 0, asdecimal=False)),
    Column('reserved5', Numeric(3, 0, asdecimal=False)),
    Index('ind_1_med_price_list', 'item_class', 'item_code', 'item_spec', 'units', 'start_date', unique=True)
)


class MedRelationshipDict(Base):
    __tablename__ = 'med_relationship_dict'

    serial_no = Column(Numeric(2, 0, asdecimal=False))
    relationship_code = Column(String(2), primary_key=True)
    relationship_name = Column(String(10))
    input_code = Column(String(8))


class MedRole(Base):
    __tablename__ = 'med_roles'

    role_id = Column(String(36), primary_key=True)
    app_id = Column(String(36), nullable=False)
    name = Column(String(60), nullable=False)
    description = Column(String(160))
    create_date = Column(DateTime, nullable=False)


class MedRolesPermission(Base):
    __tablename__ = 'med_roles_permissions'

    role_id = Column(String(36), primary_key=True, nullable=False)
    permission_id = Column(String(36), primary_key=True, nullable=False)


t_med_screen_col_list = Table(
    'med_screen_col_list', metadata,
    Column('col', String(30), nullable=False),
    Column('col_name', String(30), nullable=False),
    Column('col_width', Numeric(12, 2), nullable=False),
    Column('col_status', Numeric(1, 0, asdecimal=False)),
    Column('col_no', Numeric(3, 0, asdecimal=False))
)


class MedScreenConfig(Base):
    __tablename__ = 'med_screen_config'

    screen_dept_code = Column(String(16))
    screen_font = Column(String(100))
    screen_type = Column(Numeric(asdecimal=False), primary_key=True)
    screen_mode = Column(Numeric(asdecimal=False))
    screen_timer = Column(Numeric(asdecimal=False))
    screen_autologion = Column(Numeric(asdecimal=False))
    scerrn_width = Column(Numeric(asdecimal=False))
    screen_height = Column(Numeric(asdecimal=False))
    screen_col_color = Column(String(16))
    screen_back_color = Column(String(16))
    screen_title_color = Column(String(16))
    screen_timepage_color = Column(String(16))
    screen_shuqian_color = Column(String(16))
    screen_shuzhong_color = Column(String(16))
    screen_pacu_color = Column(String(16))
    screen_shuhou_color = Column(String(16))
    screen_temp_info = Column(String(255))
    screen_font_neirong = Column(String(100))
    screen_neirong_color = Column(String(16))
    screen_tempback_color = Column(String(16))
    screen_tempfor_color = Column(String(16))
    screen_neirongback_color = Column(String(16))
    screen_zdback_color = Column(String(16))
    screen_title = Column(String(50))
    screen_sort = Column(String(255))
    screen_firstleft = Column(Numeric(asdecimal=False))
    screen_biaoti_height = Column(Numeric(asdecimal=False))
    screen_neirong_height = Column(Numeric(asdecimal=False))


class MedScreenMsg(Base):
    __tablename__ = 'med_screen_msg'

    id = Column(String(40), primary_key=True)
    msg = Column(String(500))
    insert_time = Column(DateTime)
    counts = Column(Numeric(2, 0, asdecimal=False))
    status = Column(Numeric(1, 0, asdecimal=False))
    other1 = Column(Numeric(5, 0, asdecimal=False))
    user_id = Column(String(36))
    type = Column(Numeric(5, 0, asdecimal=False))
    dept_code = Column(String(12))


class MedScreenNewConfig(Base):
    __tablename__ = 'med_screen_new_config'

    config_key = Column(String(50), primary_key=True)
    config_value = Column(String(1000))


class MedScreenTemplate(Base):
    __tablename__ = 'med_screen_template'

    screen_col_color = Column(String(16))
    screen_back_color = Column(String(16))
    screen_title_color = Column(String(16))
    screen_timepage_color = Column(String(16))
    screen_shuqian_color = Column(String(16))
    screen_shuzhong_color = Column(String(16))
    screen_pacu_color = Column(String(16))
    screen_shuhou_color = Column(String(16))
    screen_neirong_color = Column(String(16))
    screen_neirongback_color = Column(String(16))
    screen_tempback_color = Column(String(16))
    screen_tempfor_color = Column(String(16))
    screen_zdback_color = Column(String(16))
    screen_template_no = Column(Numeric(3, 0, asdecimal=False))
    screen_template_name = Column(String(16), primary_key=True)


class MedSexDict(Base):
    __tablename__ = 'med_sex_dict'

    serial_no = Column(Numeric(1, 0, asdecimal=False))
    sex_code = Column(String(1))
    sex_name = Column(String(4), primary_key=True)
    input_code = Column(String(8))
    input_code_wb = Column(String(8))


class MedSpecificWordDict(Base):
    __tablename__ = 'med_specific_word_dict'

    word_code = Column(String(10))
    word_name = Column(String(40), primary_key=True)
    input_code = Column(String(8))


class MedStaffDict(Base):
    __tablename__ = 'med_staff_dict'

    emp_no = Column(String(6), primary_key=True)
    dept_code = Column(String(8))
    name = Column(String(30))
    input_code = Column(String(8))
    job = Column(String(8))
    title = Column(String(10))
    user_name = Column(String(30))
    in_hospital = Column(Numeric(1, 0, asdecimal=False))
    nurse_type = Column(String(8))
    verify_pw = Column(String(20))
    create_date = Column(DateTime)


class MedStaffVsGroup(Base):
    __tablename__ = 'med_staff_vs_group'

    group_class = Column(String(16), primary_key=True, nullable=False)
    group_code = Column(String(8), primary_key=True, nullable=False)
    emp_no = Column(String(6), primary_key=True, nullable=False, index=True)


class MedTitleDict(Base):
    __tablename__ = 'med_title_dict'

    serial_no = Column(Numeric(3, 0, asdecimal=False))
    title_code = Column(String(3), primary_key=True)
    title_name = Column(String(26))
    input_code = Column(String(8))


class MedTransfer(Base):
    __tablename__ = 'med_transfer'

    patient_id = Column(String(20), primary_key=True, nullable=False)
    visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    dept_stayed = Column(String(16))
    admission_date_time = Column(DateTime, primary_key=True, nullable=False)
    discharge_date_time = Column(DateTime)
    dept_transfered_to = Column(String(16))
    doctor_in_charge = Column(String(30))
    ward_stayed = Column(String(16))
    ward_transfered_to = Column(String(16))
    reserved1 = Column(Numeric(3, 0, asdecimal=False))
    bed_no = Column(String(20))
    reserved2 = Column(Numeric(3, 0, asdecimal=False))
    reserved3 = Column(DateTime)


t_med_user_permissions = Table(
    'med_user_permissions', metadata,
    Column('user_id', String(36), nullable=False),
    Column('role_id', String(36), nullable=False),
    Column('permission_id', String(36), nullable=False),
    Column('app_id', String(36), nullable=False),
    Column('name', String(100), nullable=False),
    Column('sort_id', Numeric(10, 0, asdecimal=False)),
    Column('permission_key', String(160), nullable=False),
    Column('description', String(160)),
    Column('login_name', String(36), nullable=False)
)


class MedUser(Base):
    __tablename__ = 'med_users'

    user_id = Column(String(36), primary_key=True)
    login_name = Column(String(36), nullable=False, unique=True)
    login_pwd = Column(String(36), nullable=False)
    user_name = Column(String(36))
    dept_id = Column(String(16))
    create_date = Column(DateTime)
    is_valid = Column(String(1), nullable=False, server_default=text("'T' "))
    memo = Column(String(100))


t_med_users_applications = Table(
    'med_users_applications', metadata,
    Column('app_id', String(36), nullable=False),
    Column('user_id', String(36), nullable=False)
)


class MedUsersDept(Base):
    __tablename__ = 'med_users_depts'

    user_id = Column(String(36), primary_key=True, nullable=False)
    dept_id = Column(String(16), primary_key=True, nullable=False)


class MedUsersHisuser(Base):
    __tablename__ = 'med_users_hisusers'

    user_id = Column(String(36), primary_key=True, nullable=False)
    his_user_id = Column(String(36), primary_key=True, nullable=False)
    memo = Column(String(100))


class MedUsersInouttime(Base):
    __tablename__ = 'med_users_inouttime'

    user_id = Column(String(36), primary_key=True, nullable=False)
    in_time = Column(DateTime, primary_key=True, nullable=False)
    out_time = Column(DateTime)
    cupboard = Column(String(3))


class MedUsersRole(Base):
    __tablename__ = 'med_users_roles'

    user_id = Column(String(36), primary_key=True, nullable=False)
    role_id = Column(String(36), primary_key=True, nullable=False)


t_med_users_zp = Table(
    'med_users_zp', metadata,
    Column('user_id', String(36), nullable=False),
    Column('zp', LargeBinary)
)


class MedVsHisDepId(Base):
    __tablename__ = 'med_vs_his_dep_id'

    med_patient_id = Column(String(20), primary_key=True, nullable=False)
    med_visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    med_dep_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    his_adm_ward_date_time = Column(DateTime)
    his_patient_id = Column(String(20))
    his_visit_id = Column(String(20))


class MedVsHisOperApply(Base):
    __tablename__ = 'med_vs_his_oper_apply'
    __table_args__ = (
        Index('ind_1_med_vs_his_oper_apply', 'his_apply_no', 'his_patient_id', 'his_visit_id', 'his_schedule_id'),
    )

    med_patient_id = Column(String(20), primary_key=True, nullable=False)
    med_visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    med_schedule_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    his_apply_no = Column(String(20))
    his_patient_id = Column(String(20))
    his_visit_id = Column(Numeric(10, 0, asdecimal=False))
    his_schedule_id = Column(Numeric(10, 0, asdecimal=False))
    req_date_time = Column(String(10), primary_key=True, nullable=False)


class MedVsHisOperApplyV2(Base):
    __tablename__ = 'med_vs_his_oper_apply_v2'
    __table_args__ = (
        Index('ind_1_med_vs_his_oper_apply_v2', 'his_apply_no', 'his_patient_id', 'his_visit_id', 'his_schedule_id'),
    )

    med_patient_id = Column(String(20), primary_key=True, nullable=False)
    med_visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    med_schedule_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    his_apply_no = Column(String(20))
    his_patient_id = Column(String(20))
    his_visit_id = Column(String(20))
    his_schedule_id = Column(Numeric(10, 0, asdecimal=False))
    req_date_time = Column(String(10))


class MedVsHisOperBillConst(Base):
    __tablename__ = 'med_vs_his_oper_bill_consts'

    patient_id = Column(String(20), primary_key=True, nullable=False)
    visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    oper_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    consts_count = Column(Numeric(5, 0, asdecimal=False), primary_key=True, nullable=False)
    item_no_string = Column(String(200), primary_key=True, nullable=False)
    item_no_string_indicator = Column(String(200))
    reserved1 = Column(String(500))
    reserved2 = Column(String(20))
    reserved3 = Column(String(20))


t_med_vs_his_oper_bill_items = Table(
    'med_vs_his_oper_bill_items', metadata,
    Column('med_patient_id', String(20), nullable=False),
    Column('med_visit_id', Numeric(2, 0, asdecimal=False), nullable=False),
    Column('med_oper_id', Numeric(2, 0, asdecimal=False), nullable=False),
    Column('item_no', Numeric(3, 0, asdecimal=False), nullable=False),
    Column('item_class', String(16)),
    Column('item_name', String(60)),
    Column('item_code', String(10)),
    Column('item_spec', String(20)),
    Column('amount', Numeric(6, 2)),
    Column('units', String(8)),
    Column('his_patient_id', String(20)),
    Column('his_visit_id', String(20)),
    Column('his_schedule_id', String(20)),
    Column('create_date', DateTime),
    Column('reserved01', String(20)),
    Column('reserved02', String(20)),
    Column('reserved03', String(20)),
    Column('reserved04', String(20)),
    Column('reserved05', String(20))
)


class MedVsHisOperMaster(Base):
    __tablename__ = 'med_vs_his_oper_master'
    __table_args__ = (
        Index('ind_1_med_vs_his_oper_master', 'his_apply_no', 'his_patient_id', 'his_visit_id', 'his_schedule_id'),
    )

    med_patient_id = Column(String(20), primary_key=True, nullable=False)
    med_visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    med_oper_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    his_apply_no = Column(String(20))
    his_patient_id = Column(String(20))
    his_visit_id = Column(String(20))
    his_schedule_id = Column(Numeric(10, 0, asdecimal=False))
    req_date_time = Column(String(10))


class MedVsHisOrderClas(Base):
    __tablename__ = 'med_vs_his_order_class'

    serial_no = Column(Numeric(3, 0, asdecimal=False))
    his_class_code = Column(String(16), primary_key=True)
    his_class_name = Column(String(16))
    med_class_code = Column(String(1))
    med_class_name = Column(String(8))


class MedVsHisOrder(Base):
    __tablename__ = 'med_vs_his_orders'

    med_patient_id = Column(String(20), primary_key=True, nullable=False)
    med_visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    med_order_no = Column(String(20), primary_key=True, nullable=False)
    med_order_sub_no = Column(Numeric(20, 0, asdecimal=False), primary_key=True, nullable=False)
    med_repeat_indicator = Column(Numeric(1, 0, asdecimal=False), primary_key=True, nullable=False)
    his_order_no = Column(String(20))
    his_order_sub_no = Column(String(20))
    create_date = Column(DateTime)
    reserved01 = Column(String(50))
    reserved02 = Column(String(50))
    reserved03 = Column(String(50))
    reserved04 = Column(String(50))
    reserved05 = Column(String(50))


class MedVsHisPat(Base):
    __tablename__ = 'med_vs_his_pat'
    __table_args__ = (
        Index('ind_1_med_vs_his_pat', 'his_patient_id', 'his_inp_no', 'his_visit_id'),
    )

    med_patient_id = Column(String(20), primary_key=True, nullable=False)
    med_visit_id = Column(Numeric(2, 0, asdecimal=False), primary_key=True, nullable=False)
    his_patient_id = Column(String(20))
    his_inp_no = Column(String(20))
    his_visit_id = Column(String(20))
    create_date = Column(DateTime)
    reserved01 = Column(String(50))
    reserved02 = Column(String(50))
    reserved03 = Column(String(50))
    reserved04 = Column(String(50))
    reserved05 = Column(String(50))
    reserved06 = Column(String(50))
    reserved07 = Column(String(50))
    reserved08 = Column(String(50))


class MedVsPacsExam(Base):
    __tablename__ = 'med_vs_pacs_exam'

    med_exam_no = Column(String(20), primary_key=True)
    his_item_class = Column(String(20))
    his_exam_no = Column(Numeric(10, 0, asdecimal=False))
    his_patient_local_id = Column(String(20))


class MedWoundGradeDict(Base):
    __tablename__ = 'med_wound_grade_dict'

    serial_no = Column(Numeric(1, 0, asdecimal=False))
    wound_grade_code = Column(String(1), primary_key=True)
    wound_grade_name = Column(String(2))
    input_code = Column(String(8))


t_view_operation_list = Table(
    'view_operation_list', metadata,
    Column('patient_id', String(20)),
    Column('visit_id', Numeric(2, 0, asdecimal=False)),
    Column('schedule_id', Numeric(2, 0, asdecimal=False)),
    Column('name', String(30)),
    Column('sex', String(4)),
    Column('inp_no', String(20)),
    Column('date_of_birth', DateTime),
    Column('nation', String(30)),
    Column('dept_stayed', String(40)),
    Column('bed_no', String(20)),
    Column('scheduled_date_time', DateTime),
    Column('operating_room', String(16)),
    Column('operating_room_name', String(40)),
    Column('operating_room_no', String(8)),
    Column('sequence', Numeric(2, 0, asdecimal=False)),
    Column('diag_before_operation', String(80)),
    Column('patient_condition', String(100)),
    Column('operation', String(100)),
    Column('operation_scale', String(2)),
    Column('operating_dept', String(40)),
    Column('surgeon', String(30)),
    Column('first_assistant', String(30)),
    Column('second_assistant', String(30)),
    Column('third_assistant', String(30)),
    Column('fourth_assistant', String(30)),
    Column('anesthesia_method', String(60)),
    Column('anesthesia_doctor', String(30)),
    Column('anesthesia_assistant', String(30)),
    Column('second_anesthesia_doctor', String(30)),
    Column('third_anesthesia_doctor', String(30)),
    Column('fourth_anesthesia_assistant', String(30)),
    Column('first_operation_nurse', String(30)),
    Column('second_operation_nurse', String(30)),
    Column('first_supply_nurse', String(30)),
    Column('second_supply_nurse', String(30)),
    Column('third_supply_nurse', String(30)),
    Column('notes_on_operation', String(100)),
    Column('entered_by', String(20)),
    Column('req_date_time', DateTime),
    Column('emergency_indicator', Numeric(1, 0, asdecimal=False)),
    Column('operation_position', String(32)),
    Column('reserved4', String(20)),
    Column('reserved5', String(20)),
    Column('type', String(6)),
    Column('oper_status', Numeric(asdecimal=False)),
    Column('pat_age', Numeric(asdecimal=False))
)
