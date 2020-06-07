# coding:utf-8
import requests
import pytest
import sys
import os
import configparser
sys.path.append('../')
from util.handle_json import handle_jsonData
from util.handle_init import handle_ini
from base.base_request import baseRequest

baseFileName = '/ApiTestProject/Apiautomation/test_data/getrequest.json'


class TestOne():
    def test_requestOne(self):
        baseurl = handle_ini.get_value('apiurl', 'imooc')
        url = baseurl + handle_jsonData.getJson_value('url', baseFileName)
        method = handle_jsonData.getJson_value('method',baseFileName)
        header = handle_jsonData.getJson_value('headers', baseFileName)
        paramsData = handle_jsonData.getJson_value('params', baseFileName)
        #result = requests.get(url=url, headers = header, params=paramsData).json()
        responseData = baseRequest.run_main(method,url,paramsData,"",header)
        print(responseData)


if __name__ == "__main__":
    pytest.main(["-s", "test_one.py"])
