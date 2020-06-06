# coding:utf-8
import requests
import pytest
import sys
import os
import configparser
sys.path.append('../')
from util.handle_init import handle_ini


class TestOne():
    def test_requestOne(self):
        baseurl = handle_ini.get_value('apiurl', 'imooc')
        url = baseurl+'/search/history'
        print(url)
        result = requests.get(url=url, params={'wrods': 'Test'}).json()
        print(result)


if __name__ == "__main__":
    pytest.main(["-s", "test_one.py"])
