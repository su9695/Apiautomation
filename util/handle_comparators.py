# coding:utf-8
import sys
import os
sys.path.append('../')
sys.path.append('D:/ApiAuto/Apiautomation')
curPath = os.path.abspath(os.path.dirname(__file__))

class comparators():
    def assertEqual(self, result, check, expect):
        result_data = result.json()
        if check == 'status_code':
            assert str(result.status_code) == expect
        else:
            assert result_data[check] == expect

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
