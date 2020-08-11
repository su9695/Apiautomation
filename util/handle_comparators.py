# coding:utf-8
import pytest
import json
import sys
import os


class comparators():
    def assertEqual(self, result, check, expect):
        assert result[check] == expect

    def comparators_Assert(self, result, check, comparator, expect):
        if (comparator in ["eq", "equals", "equal"]):
            self.assertEqual(result, check, expect)

comparatorsTest = comparators()

# if __name__ == "__main__":
#     result = {'result': 0, 'data': [{'word': 'testng'}, {'word': 'test'}, {'word': 'testlink'}, {'word': 'testn'},
#                                     {'word': 'testng教程'}], 'msg': '成功'}
#     check = 'msg'
#     comparator = "eq"
#     expect = "成功"
#     comparatorsTest = comparators()
#     comparatorsTest.comparators_Assert(result, check, comparator, expect)
