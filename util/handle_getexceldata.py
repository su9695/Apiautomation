# coding:utf-8
from util.handle_exceldata import OperationExcel
from util.handle_excelconfig import *
import sys
import os

sys.path.append('../')
sys.path.append('D:/ApiAuto/Apiautomation')
curPath = os.path.abspath(os.path.dirname(__file__))

class GetData:
    def __init__(self, file_name, sheet_id):
        self.opera_excel = OperationExcel(file_name, sheet_id)

    # 去获取excel行数,就是我们的case个数
    def get_case_lines(self):
        return self.opera_excel.get_lines()

    # 获取接口模块名
    def get_name(self, row):
        col = int(get_request_name())
        request_name = self.opera_excel.get_cell_value(row, col)
        return request_name

    # 获取是否执行
    def get_is_run(self, row):
        flag = None
        col = int(get_run())
        run_model = self.opera_excel.get_cell_value(row, col)
        if run_model.lower() == 'yes':
            flag = True
        else:
            flag = False
        return flag

    # 获取请求方式
    def get_request_method(self, row):
        col = int(get_method())
        request_method = self.opera_excel.get_cell_value(row, col)
        return request_method

    # 获取url
    def get_request_url(self, row):
        col = int(get_url())
        url = self.opera_excel.get_cell_value(row, col)
        return url

    # 获取请求数据
    def get_request_data(self, row):
        col = int(get_request_data())
        data = self.opera_excel.get_cell_value(row, col)
        if data == '':
            return None
        return data

    # 获取预期结果
    def get_expcet_data(self, row):
        col = int(get_expect())
        expect = self.opera_excel.get_cell_value(row, col)
        if expect == '':
            return None
        return expect

    def write_result(self, row, value):
        col = int(get_result())
        self.opera_excel.write_value(row, col, value)

    def write_pass(self, row, value):
        col = int(get_is_pass())
        self.opera_excel.write_value(row, col, value)
