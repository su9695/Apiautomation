# coding:utf-8
import pytest
import sys
import os
import allure
import json

curPath = os.path.abspath(os.path.dirname(__file__))
root_path = os.path.abspath(os.path.dirname(curPath) + os.path.sep + "../")
sys.path.append(root_path)
os.chdir(root_path)

from util.handle_json import handle_jsonData
from util.handle_init import handle_ini
from util.handle_log import run_log as logger
from util.handle_apirequest import apiRequest
from pactverify.matchers import Matcher, Like, EachLike, Term, Enum, PactVerify
from util.handle_comparators import comparatorsTest

baseurl = handle_ini.get_value('apiurl', 'imooc')
baseFileName = root_path + '/test_data/jsondata/testRequest/getRequest.json'
testCaseData = handle_jsonData.load_json(baseFileName)

@allure.feature('测试GET请求模块')
class TestRequestOne():
    @allure.title('测试标题')
    @allure.testcase('测试地址：https://www.imooc.com')
    @pytest.mark.parametrize('case_data', testCaseData['testcase'])
    def test_requestOne(self, case_data):
        try:
            api_response = apiRequest.api_request(baseurl, testCaseData, case_data)
            api_response_data = api_response.json()
            # pactverity——全量契约校验
            config_contract_format = Like({
                "msg": "成功",
                "result": 0,
                "data": EachLike({
                    "word": Like("testng")
                })
            })
            mPactVerify = PactVerify(config_contract_format)
            try:
                mPactVerify.verify(api_response_data)
                logger.info(
                    'verify_result：{}，verify_info:{}'.format(mPactVerify.verify_result, mPactVerify.verify_info))
                assert mPactVerify.verify_result == True
            except Exception:
                err_msg = '契约校验错误'
                logger.exception('测试用例契约校验失败，verify_result：{}，verify_info:{}'.format(mPactVerify.verify_result,
                                                                                     mPactVerify.verify_info))
            try:
                for case_validate in case_data['validate']:
                    logger.info('断言期望相关参数：check：{},comparator：{},expect：{}'.format(case_validate['check'],
                                                                                   case_validate['comparator'],
                                                                                   case_validate['expect']))
                    comparatorsTest.comparators_Assert(api_response, case_validate['check'],
                                                       case_validate['comparator'], case_validate['expect'])
                    logger.info('测试用例断言成功')
            except Exception as e:
                logger.exception('测试用例断言失败')
        except Exception as e:
            logger.exception('测试用例请求失败，原因：{}'.format(e))


# 调用class
TestRequestOne()

if __name__ == "__main__":
    # 生成配置信息 "-s 代表可以将执行成功的案例日志打印出来 ; -q+文件执行路径 代表只需要执行的文件"
    pytest.main(['-s', '-v', 'test_case/testRequest/test_getRequestJson.py', '-q', '--alluredir', 'reports'])
