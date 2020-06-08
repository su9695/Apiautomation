# coding:utf-8
import sys
import os
import configparser
sys.dont_write_bytecode = True
sys.path.append('../')
from Apiautomation.util.handle_json import handle_jsonData


class HandleHeader:
    # 获取header值，json文件中读取不到，则返回默认header值
    def get_header(self, file_name):
        headerData = handle_jsonData.getJson_value("headers", file_name)
        return headerData


handle_headerData = HandleHeader()
# if __name__ == "__main__":
#     headerjson = HandleHeader()
#     headerjson.get_header(
#         '/ApiTestProject/Apiautomation/test_data/getrequest.json')