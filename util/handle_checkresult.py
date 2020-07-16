# coding=utf-8
import sys
import json
from util.handle_log import run_log as logger

sys.path.append('../')


class HandleCheckResult:

    def check_result(self, apiResponseData, case_data):
        """
        校验测试结果
        :return:
        """
        try:
            comparator = case_data['validate'][0]['comparator']
            check = case_data['validate'][0]['check']
            expect = case_data['validate'][0]['expect']
            apicheck = apiResponseData[check]
            print(expect)
            #print(apicheck)
            if (comparator == 'eq'):
                pass
        except Exception as e:
            logger.exception('测试用例对比失败，{}'.format(e))
        pass


# handle_check_Result = HandleCheckResult()

if __name__ == '__main__':
    handle_check_Result = HandleCheckResult()
    apiResponseData = {"result": 0,
                       "data": [{"word": "testng"}, {"word": "test"}, {"word": "testlink"}, {"word": "testn"},
                                {"word": "testng教程"}], "msg": "成功"}
    case_data = {"name": "测试用例1", "params": {"words": "Test"},
                 "validate": [{"check": "msg", "comparator": "eq", "expect": "成功"}]}
    handle_check_Result.check_result(apiResponseData, case_data)
