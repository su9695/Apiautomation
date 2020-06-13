# coding:utf-8
import requests
import pytest
import json
import sys
import os
import configparser
import allure
sys.path.append('../')


if __name__ == "__main__":
    pytest.main(['-s','-v','../test_case','-q', '--alluredir', '../reports'])
