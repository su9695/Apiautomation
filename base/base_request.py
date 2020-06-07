# coding:utf-8
import requests
import json
import pytest
import sys
import os
import configparser
sys.path.append('../')
from Apiautomation.util.handle_init import handle_ini
from Apiautomation.util.handle_json import handle_jsonData

class BaseRequest:
    # Requests发送Get请求
    def send_get(self, url, data, cookie=None, header=None):
        response = requests.get(url=url, params=data, headers=header)
        return response

    # Requests发送Post请求
    def send_post(self, url, data, cookie=None, header=None):
        response = requests.post(url=url, data=data, headers=header)
        return response

    def run_main(self,method,url,data,cookie=None,header=None):
        if method == 'get':
            result = self.send_get(url,data,header)
        else:
            result = self.send_post(url,data,header)
        try:
            res = result.json()
        except Exception:
            res = {}
        return res

baseRequest =BaseRequest()
# if __name__ == "__main__":
#     baseRequest =BaseRequest()
#     result = baseRequest.run_main('get','https://www.imooc.com/search/history',"{'words':'Test'}","","{'Content-Type': 'application/json'}")
#     print(result)