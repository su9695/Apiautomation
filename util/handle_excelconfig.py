# coding=utf-8
# 封装Excel表中的常量方法
class global_var:
    # case_id
    Id = '0'
    modular = '1'
    run = '2'
    preconditions = '3'
    request_name = '4'
    request_type = '5'
    url = '6'
    header = '7'
    cookie = '8'
    case_depend = '9'
    data_depend = ''
    field_depend = ''
    request_data = ''
    result = '11'


def get_id():
    return global_var.Id

def get_modular():
    return global_var.modular

def get_run():
    return global_var.run

def get_preconditions():
    return global_var.preconditions

def get_request_name():
    return global_var.request_name

def get_request_type():
    return global_var.request_type

def get_url():
    return global_var.url

def get_header():
    return global_var.header

def get_cookie():
    return global_var.cookie

def get_case_depend():
    return global_var.case_depend

def get_data_depend():
    return global_var.data_depend

def get_field_depend():
    return global_var.field_depend

def get_result_data():
    return global_var.result_data

def get_result():
    return global_var.result
