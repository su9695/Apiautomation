# coding:utf-8
import sys
import os
import configparser
sys.path.append('../')

class HandleInit:
    # 读取配置文件
    def load_ini(self):
        file_path = "/ApiTestProject/Apiautomation/config/server.ini"
        cf = configparser.ConfigParser()
        cf.read(file_path, encoding='UTF-8')
        return cf

    # 获取ini里面对应key的value
    def get_value(self, key, node=None):
        if node == None:
            node = 'Test'
        cf = self.load_ini()
        try:
            data = cf.get(node, key)
        except Exception:
            print("没有获取到对应的值")
            data = None
        return data


handle_ini = HandleInit()
# if __name__ == "__main__":
#     he =  HandleInit()
#     print(he.get_value('apiurl','imooc'))
