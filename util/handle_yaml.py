# coding=utf-8
import sys
import yaml
import os

sys.path.append('../')
sys.path.append('D:/ApiAuto/Apiautomation')
curPath = os.path.abspath(os.path.dirname(__file__))

class HandleYaml:
    # 读取yaml文件
    def load_yaml(self, file_name):
        if file_name == None:
            file_path = ""
        else:
            file_path = file_name
        try:
            with open(file_path, encoding='UTF-8') as f:
                data = yaml.load(f, Loader=yaml.FullLoader)
            return data
        except Exception:
            print("未找到yaml文件")
            return {}

    # 读取yaml文件里具体的字段值
    def getYaml_Data(self, file_name):
        if file_name == None:
            return ""
        yamlData = self.load_yaml(file_name)
        return yamlData


handle_YamlData = HandleYaml()
# if __name__ == "__main__":
#     hyaml = HandleYaml()
#     params = hyaml.getYaml_value('../test_data/yamldata/getRequest.yml')
#     print(params)
