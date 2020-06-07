# coding:utf-8
import requests
import pytest
import json
import sys
import os
import configparser
sys.path.append('../')
from Apiautomation.util.handle_json import handle_jsonData
from Apiautomation.util.handle_init import handle_ini
from Apiautomation.base.base_request import baseRequest
from Apiautomation.util.log import run_log as logger

baseFileName = '/ApiTestProject/Apiautomation/test_data/getRequest.json'


class TestOne():
    def test_requestOne(self):
        baseurl = handle_ini.get_value('apiurl', 'imooc')
        url = baseurl + handle_jsonData.getJson_value('url', baseFileName)
        method = handle_jsonData.getJson_value('method',baseFileName)
        header = handle_jsonData.getJson_value('headers', baseFileName)
        paramsData = handle_jsonData.getJson_value('params', baseFileName)
        responseData = baseRequest.run_main(method,url,paramsData,"",header)
        assert responseData['msg'] == "成功"
        assert responseData['data'][0]['word'] == "python"
        logger.error("测试日志模块")

if __name__ == "__main__":
    pytest.main(["-s", "test_one.py"])
