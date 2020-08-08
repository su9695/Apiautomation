# coding:utf-8
import pytest
import json
import sys
import os
import allure
import atexit

sys.path.append('../')
sys.path.append('../Apiautomation')
curPath = os.path.abspath(os.path.dirname(__file__))
BasePath = curPath[:curPath.find("Apiautomation\\") + len("Apiautomation\\")]
from util.handle_json import handle_jsonData
from util.handle_init import handle_ini
from util.handle_log import run_log as logger
from util.handle_apirequest import apiRequest
from pactverify.matchers import Matcher, Like, EachLike, Term, Enum, PactVerify

baseurl = handle_ini.get_value('blackListBaseUrl', 'blackList')
baseFileName = BasePath + '/test_data/jsondata/blackList/blackReason.json'
testCaseData = handle_jsonData.load_json(baseFileName)


@allure.feature('黑名单模块')
class TestRequestOne():
    @allure.title('拉黑原因列表接口')
    @allure.testcase('黑名单地址：http://tcwlservice.17usoft.com/csc/api/blackList')
    @pytest.mark.parametrize('case_data', testCaseData['testcase'])
    def test_requestOne(self, case_data):
        try:
            apiResponseData = apiRequest.api_request(baseurl, testCaseData, case_data)

            # pactverity——全量契约校验
            config_contract_format = Like({
                "code": 10000,
                "msg": "ok",
                "data": EachLike({
                    "id": 148,
                    "reason": "恶意套取信息",
                    "productId": 0,
                    "sourceType": 0,
                    "channelType": 1,
                    "blackTerm": Like({'': ''}, nullable=True)
                })
            })
            mPactVerify = PactVerify(config_contract_format)
            try:
                pass
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


# 调用class
TestRequestOne()

if __name__ == "__main__":
    #     # 生成配置信息 "-s 代表可以将执行成功的案例日志打印出来 ; -q+文件执行路径 代表只需要执行的文件"
    #     pytest.main(['-s', '-v', 'isBlack.py', '-q', '--alluredir', '../reports/result'])
    pytest.main(['-v', 'blackReason.py'])
