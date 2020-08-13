# coding=utf-8
import sys
import os
import json
import pytest
import allure

curPath = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "../")
sys.path.append(root_path)
os.chdir(root_path)
from util.handle_getexceldata import GetData
from base.base_request import baseRequest
from util.handle_init import handle_ini
from util.handle_log import run_log as logger

file_name = 'D:/ApiAuto/Apiautomation/test_data/exceldata/case1.xls'
sheet_id = 0


@allure.feature('测试Excel模块')
class TestMainExcel():
    @allure.title('测试标题')
    @allure.testcase('测试地址：https://www.imooc.com')
    def test_mainExcel(self):
        excelData = GetData(file_name, sheet_id)
        rows_count = excelData.get_case_lines()
        for i in range(1, rows_count):
            is_run = excelData.get_is_run(i)
            if is_run:
                url = excelData.get_request_url(i)
                method = excelData.get_request_method(i)
                request_data = json.loads(excelData.get_request_data(i))
                header = json.loads(handle_ini.get_value('headerDefault', 'header'))
                expect = excelData.get_expcet_data(i)
                with allure.step('接口请求信息：'):
                    allure.attach('接口名：{},接口请求地址：{}，接口请求方式：{}，接口请求参数：{}'.format(excelData.get_name(i), url, method, request_data))
                res = baseRequest.run_main(method, url, request_data, header)
                res_data = res.json()
                excelData.write_result(i, json.dumps(res_data, ensure_ascii=False))
                try:
                    assert json.loads(expect) == res_data
                    excelData.write_pass(i, 'PASS')
                except Exception as e:
                    excelData.write_pass(i, 'NO')


TestMainExcel()

# if __name__ == "__main__":
#     pytest.main(['-s', '-v', 'test_mainExcel.py', '-q', '--alluredir', '../../reports/result'])
#     # pytest.main(['-s', '-v', 'test_mainExcel.py'])
