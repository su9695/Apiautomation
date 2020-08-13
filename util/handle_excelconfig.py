# coding:utf-8
import sys
import os

sys.path.append('../')
sys.path.append('D:/ApiAuto/Apiautomation')
curPath = os.path.abspath(os.path.dirname(__file__))

class global_var:
    Id = '0'
    request_name = '1'
    run = '2'
    url = '3'
    method = '4'
    request_data = '5'
    expect = '6'
    result = '7'
    is_pass = '8'


# 获取case编号caseid
def get_id():
    return global_var.Id


# 获取模块名request_name
def get_request_name():
    return global_var.request_name


# 获取是否执行run
def get_run():
    return global_var.run


# 获取url
def get_url():
    return global_var.url


# 获取method
def get_method():
    return global_var.method


# 获取请求参数request_data
def get_request_data():
    return global_var.request_data


# 获取预期结果expect
def get_expect():
    return global_var.expect


# 获取实际结果result
def get_result():
    return global_var.result


# 获取是否通过is_pass
def get_is_pass():
    return global_var.is_pass
