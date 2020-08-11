# coding:utf-8
import pytest
import sys
import os

sys.path.append('../')
curPath = os.path.abspath(os.path.dirname(__file__))
BasePath = curPath[:curPath.find("Apiautomation\\") + len("Apiautomation\\")]

if __name__ == "__main__":
    pytest.main(['-s', '-v', 'test_case/testRequest/', '-q', '--alluredir', 'Apiautomation/reports'])
