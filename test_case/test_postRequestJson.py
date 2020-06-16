# coding:utf-8
import requests
import pytest
import json
import sys
import os
import configparser
import allure
sys.path.append('../')
curPath = os.path.abspath(os.path.dirname(__file__))
BasePath = curPath[:curPath.find("Apiautomation\\")+len("Apiautomation\\")]
from util.handle_json import handle_jsonData
from util.handle_init import handle_ini
from base.base_request import baseRequest
from util.handle_log import run_log as logger

baseFileName = BasePath + '/test_data/jsondata/postRequest.json'


@allure.epic('测试描述'.center(30, '*'))
@allure.feature('测试模块')
@allure.suite('测试套件')
class TestRequestOne():
    @allure.story('用户故事描述')
    @allure.title('测试标题')
    @allure.description('测试用例描述')
    @allure.testcase('测试用例地址:https://fanyi.baidu.com')
    def test_requestOne(self):
        
        try:
            baseurl = handle_ini.get_value('baidufanyiurl', 'baidu')
            url = baseurl + handle_jsonData.getJson_value('url', baseFileName)
            method = handle_jsonData.getJson_value('method', baseFileName)
            header = handle_jsonData.getJson_value('headers', baseFileName)
            paramsData = handle_jsonData.getJson_value('params', baseFileName)
            responseData = baseRequest.run_main(
                method, url, paramsData, header)
            assert responseData['msg'] == "success"
            #assert responseData['data'][0]['word'] == "python"
            logger.info('接口请求地址url：%r，请求方法：%r，请求header：%r，请求参数：%r，请求返回：%r' % (
                url, method, header, paramsData, responseData))
        except Exception as e:
            logger.error(e)

# 调用class
TestRequestOne()

if __name__ == "__main__":
    #pytest.main()
    pytest.main(['-s','-v','test_postRequestJson.py','-q', '--alluredir', '../reports'])
