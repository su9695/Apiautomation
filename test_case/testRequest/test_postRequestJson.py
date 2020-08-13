# coding:utf-8
import pytest
import json
import sys
import os
import allure

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

baseurl = handle_ini.get_value('baidufanyiurl', 'baidu')
baseFileName = root_path + '/test_data/jsondata/testRequest/postRequest.json'
testCaseData = handle_jsonData.load_json(baseFileName)


@allure.feature('测试POST请求模块')
class TestRequestOne():
    @allure.title('测试标题')
    @allure.testcase('测试地址：https://fanyi.baidu.com')
    @pytest.mark.parametrize('case_data', testCaseData['testcase'])
    def test_requestOne(self, case_data):
        try:
            api_response = apiRequest.api_request(baseurl, testCaseData, case_data)
            # pactverity——全量契约校验
            config_contract_format = Like({
                "error": 0,
                "msg": 'success',
                "lan": 'en'
            })
            mPactVerify = PactVerify(config_contract_format)
            try:
                mPactVerify.verify(api_response.json())
                logger.info(
                    'verify_result：{}，verify_info:{}'.format(mPactVerify.verify_result, mPactVerify.verify_info))
                assert mPactVerify.verify_result == True
            except Exception as e:
                logger.exception(
                    '测试用例契约校验失败，verify_result：{}，verify_info:{}，exception:{}'.format(mPactVerify.verify_result,
                                                                                     mPactVerify.verify_info, e))
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
            logger.exception('测试用例请求失败，{}'.format(e))


# 调用class
TestRequestOne()

# if __name__ == "__main__":
#     pytest.main(['-s', '-v', 'test_postRequestJson.py', '-q', '--alluredir', '../../reports/result'])
#     # pytest.main(['-v', 'test_postRequestJson.py'])
