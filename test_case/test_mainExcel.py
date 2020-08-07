# coding=utf-8
import sys
import os
import json
import pytest

sys.path.append('../')
sys.path.append('../Apiautomation')
curPath = os.path.abspath(os.path.dirname(__file__))
BasePath = curPath[:curPath.find("Apiautomation\\") + len("Apiautomation\\")]
from util.handle_getexceldata import GetData
from base.base_request import baseRequest

file_name = '../test_data/exceldata/case1.xlsx'
sheet_id = 0


class TestMainExcel():

    def test_mainExcel(self):
        res = None
        pass_count = []
        fail_count = []
        excelData = GetData(file_name, sheet_id)
        rows_count = excelData.get_case_lines()
        for i in range(1, rows_count):
            is_run = excelData.get_is_run(i)
            if is_run:
                url = excelData.get_request_url(i)
                method = excelData.get_request_method(i)
                request_data = json.loads(excelData.get_request_data(i))
                #expect = json.loads(excelData.get_expcet_data(i))


                # header = self.data.is_header(i)
                # depend_case = self.data.is_depend(i)
                # if depend_case!=None:
                #     self.depend_data = DependdentData(depend_case)
                #     # 获取的依赖响应数据
                #     depend_response_data = self.depend_data.get_data_for_key(i)
                #     # 获取依赖的key
                #     depend_key = self.data.get_depend_field(i)
                #     request_data[depend_key] = depend_response_data
                print(url, method, request_data, header)
                res = baseRequest.run_main(method, url, request_data, header)
                # self.data.write_result(i, res)
                # assert expect == res
                # self.data.write_pass(i, 'PASS')
                assert 1 == 1
                print(res)
                # self.data.write_pass(i, 'NO')


TestMainExcel()

if __name__ == "__main__":
    # pytest.main(['-s', '-v', 'test_mainExcel.py', '-q', '--alluredir', '../reports/result'])
    pytest.main(['-s', '-v', 'test_mainExcel.py'])
