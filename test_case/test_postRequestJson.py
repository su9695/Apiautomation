# coding:utf-8
import pytest
import json
import sys
import os
import allure

sys.path.append('../')
sys.path.append('../Apiautomation')
curPath = os.path.abspath(os.path.dirname(__file__))
BasePath = curPath[:curPath.find("Apiautomation\\") + len("Apiautomation\\")]
from util.handle_json import handle_jsonData
from util.handle_init import handle_ini
from base.base_request import baseRequest
from util.handle_log import run_log as logger
from util.handle_apirequest import apiRequest
from pactverify.matchers import Matcher, Like, EachLike, Term, Enum, PactVerify
from pact import Consumer, Provider

baseurl = handle_ini.get_value('baidufanyiurl', 'baidu')
baseFileName = BasePath + '/test_data/jsondata/postRequest.json'
testCaseData = handle_jsonData.load_json(baseFileName)


@allure.feature('测试模块')
class TestRequestOne():
    @allure.title('测试标题')
    @allure.testcase('测试地址：https://fanyi.baidu.com')
    @pytest.mark.parametrize('case_data', testCaseData['testcase'])
    def test_requestOne(self, case_data):
        try:
            apiResponseData = apiRequest.api_request(baseurl, testCaseData, case_data)
            # pactverity——全量契约校验
            config_contract_format = Like({
                "error": 0,
                "msg": 'success',
                "lan": 'en'
            })
            mPactVerify = PactVerify(config_contract_format)
            try:
                mPactVerify.verify(apiResponseData)
                logger.info(
                    'verify_result：{}，verify_info:{}'.format(mPactVerify.verify_result, mPactVerify.verify_info))
                assert mPactVerify.verify_result == True
            except Exception:
                err_msg = '契约校验错误'
                logger.exception('测试用例契约校验失败，verify_result：{}，verify_info:{}'.format(mPactVerify.verify_result,
                                                                                     mPactVerify.verify_info))
        except Exception as e:
            logger.exception('测试用例请求失败，{}'.format(e))
        except Exception as e:
            logger.exception('测试用例请求失败，{}'.format(e))


# 调用class
TestRequestOne()

# if __name__ == "__main__":
#     pytest.main(['-s', '-v', 'test_postRequestJson.py', '-q', '--alluredir', '../reports/result'])
