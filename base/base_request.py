# coding:utf-8
import requests


class BaseRequest:

    def send_get(self, url, data, cookie=None, header=None):
        """
        Requests发送Get请求
        :param url：请求地址
        :param data：Get请求参数
        :param cookie：cookie参数
        :param header：header参数
        """
        response = requests.get(url=url, params=data, headers=header)
        return response

    def send_post(self, url, data, cookie=None, header=None):
        """
        Requests发送Post请求
        :param url：请求地址
        :param data：Post请求参数
        :param data：Post请求参数
        :param cookie：cookie参数
        :param header：header参数
        """
        response = requests.post(url=url, data=data, headers=header)
        return response

    # 主函数调用
    def run_main(self, method, url, data, cookie=None, header=None):
        print(method, url, data)
        if method.upper() == 'GET':
            result = self.send_get(url, data, header)
        elif method.upper() == 'POST':
            result = self.send_post(url, data, header)
        try:
            res = result.json()
        except Exception:
            res = {}
        return res


# 实例
baseRequest = BaseRequest()

# if __name__ == "__main__":
#     baseRequest =BaseRequest()
#     result = baseRequest.run_main('get','https://www.imooc.com/search/history',"{'words':'Test'}","","{'Content-Type': 'application/json'}")
#     print(result)
