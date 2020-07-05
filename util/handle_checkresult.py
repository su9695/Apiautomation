# coding=utf-8
import sys
import json
from util.handle_log import run_log as logger

sys.path.append('../')


class HandleCheckResult:

    def check_result(self, apiResponseData,case_data):
        """
        校验测试结果
        :return:
        """
        try:
            
            pass
        except Exception as e:
            logger.exception('测试用例对比失败，{}'.format(e))
        pass


handle_check_Result = HandleCheckResult()