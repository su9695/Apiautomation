# coding:utf-8
class global_var:
    # case_id
    Id = '0'
    request_name = '1'
    run = '2'
    case_depend = '3'

    # data_depend = '4'
    field_depend = '4'
    url = '5'
    method = '6'
    request_data = '7'
    request_cookie = '8'
    expect = '9'
    result = '10'
    is_pass = '11'


# 获取case编号caseid
def get_id():
    return global_var.Id


# 获取模块名request_name
def get_request_name():
    return global_var.request_name


# 获取是否执行run
def get_run():
    return global_var.run


# 获取case依赖case_depend
def get_case_depend():
    return global_var.case_depend


def get_data_depend():
    return global_var.data_depend


def get_field_depend():
    return global_var.field_depend


# 获取url
def get_url():
    return global_var.url


# 获取method
def get_method():
    return global_var.method


# 获取请求参数request_data
def get_request_data():
    return global_var.request_data


# 获取cookie request_cookie
def get_request_cookie():
    return global_var.request_cookie


# 获取预期结果expect
def get_expect():
    return global_var.expect


# 获取实际结果result
def get_result():
    return global_var.result


# 获取是否通过is_pass
def get_is_pass():
    return global_var.is_pass
