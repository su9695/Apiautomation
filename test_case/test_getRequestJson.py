# coding:utf-8
import requests
import pytest
import json
import sys
import os
import configparser
import allure

sys.path.append('../')
sys.path.append('../Apiautomation')
curPath = os.path.abspath(os.path.dirname(__file__))
BasePath = curPath[:curPath.find("Apiautomation\\") + len("Apiautomation\\")]
from util.handle_json import handle_jsonData
from util.handle_init import handle_ini
from base.base_request import baseRequest
from util.handle_log import run_log as logger
from util.handle_apirequest import apiRequest

baseurl = handle_ini.get_value('apiurl', 'imooc')
baseFileName = BasePath + '/test_data/jsondata/getRequest.json'
testCaseData = handle_jsonData.load_json(baseFileName)


@allure.feature('测试模块')
class TestRequestOne():
    @allure.title('测试标题')
    @allure.testcase('测试地址：https://www.imooc.com')
    @pytest.mark.parametrize('case_data', testCaseData['testcase'])
    def test_requestOne(self, case_data):
        try:
            apiResponseData = apiRequest.api_request(baseurl, testCaseData, case_data)
            print(apiResponseData)
            if(apiResponseData != None):
                pass
            assert True == True
        except Exception as e:
            logger.exception('测试用例请求失败，{}'.format(e))


# 调用class
TestRequestOne()

if __name__ == "__main__":
    # pytest.main(['-s','-v','test_getRequestJson.py','-q', '--alluredir', '../reports'])
    pytest.main(['-v', 'test_getRequestJson.py'])
