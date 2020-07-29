# coding:utf-8
import pytest
import json
import sys
import os


class checkResult():

    def equal(self, expected_result, actual_results):
        assert expected_result == actual_results

    def checkResultType(self, check, comparator, expect, result):
        if (comparator == "eq"):
            return self.equal(result[check], expect)


if __name__ == "__main__":
    check = checkResult()
    result = {'result': 0, 'data': [{'word': 'python'}, {'word': 'python入门'}, {'word': 'python爬虫'}, {'word': 'python3'},
                                    {'word': 'python数据分析'}], 'msg': '成功'}
    print(check.checkResultType("msg", "eq", "不成功", result))
