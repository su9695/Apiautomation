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

baseFileName = BasePath + '/test_data/jsondata/getRequest.json'
testcaseData = handle_jsonData.load_json(baseFileName)

class ApiRequest():

    def api_request(self,case_data):
        pass



apiRequest = ApiRequest()

# if __name__ == '__main__':
#     case_data = []
#     apiRequest = ApiRequest()
#     apiRequest.api_request(case_data)