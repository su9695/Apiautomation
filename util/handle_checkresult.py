# coding=utf-8
import sys
import json

sys.path.append('../')


class HandleCheckResult:

    def check_result(self, test_name, case, code, data, _path, relevance=None):
        """
        校验测试结果
        :param test_name: 测试名称
        :param case: 测试用例
        :param code: HTTP状态
        :param data: 返回的接口json数据
        :param relevance: 关联值对象
        :param _path: case路径
        :return:
        """
        pass
