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
BasePath = curPath[:curPath.find("Apiautomation\\")+len("Apiautomation\\")]
from util.handle_yaml import handle_YamlData
from util.handle_init import handle_ini
from base.base_request import baseRequest
from util.handle_log import run_log as logger

baseFileName = BasePath + '/test_data/yamldata/getRequest.yml'

class TestRequestOne():
    def test_requestOne(self):
        try:
            baseurl = handle_ini.get_value('apiurl', 'imooc')
            logger.info(baseurl)
            yamldata = handle_YamlData.load_yaml(baseFileName)
            return yamldata
        except Exception as e:
            logger.error(e)


# 调用class
#TestRequestOne()

if __name__ == '__main__':
    func = TestRequestOne()
    data = func.test_requestOne()
    print(data)