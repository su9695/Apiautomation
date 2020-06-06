# coding:utf-8
import requests
import pytest
import sys
import os
import configparser
sys.path.append('../')
from util.handle_init import handle_ini

class BaseRequest:
    # Requests发送Get请求
    def send_get(self,url,data,cookie=None,header=None):
        pass


    # Requests发送Post请求
    def send_post(self,url,data,cookie=None,header=None):
        pass


