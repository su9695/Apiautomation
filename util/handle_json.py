# coding=utf-8
import sys
import json
import os

sys.path.append('../')
sys.path.append('D:/ApiAuto/Apiautomation')
curPath = os.path.abspath(os.path.dirname(__file__))


class HandleJson:
    # 读取json文件
    def load_json(self, file_name):
        if file_name == None:
            file_path = ""
        else:
            file_path = file_name
        try:
            with open(file_path, encoding='UTF-8') as f:
                data = json.load(f)
            return data
        except Exception:
            print("未找到json文件")
            return {}

    # 读取json文件里具体的字段值
    def getJson_value(self, key, file_name):
        if file_name == None:
            return ""
        jsonData = self.load_json(file_name)
        if key == None:
            getJsonValue = ""
        else:
            getJsonValue = jsonData.get(key)
        return getJsonValue


handle_jsonData = HandleJson()
# if __name__ == "__main__":
#     hjson = HandleJson()
#     params = hjson.getJson_value(
#         "params", '/ApiTestProject/Apiautomation/test_data/jsondata/getrequest.json')
#     print(params)
