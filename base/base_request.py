# coding:utf-8
import requests
import allure
import json
from util.handle_log import run_log as logger


class BaseRequest:

    def send_get(self, url, data, header=None, cookie=None):
        """
        Requests发送Get请求
        :param url：请求地址
        :param data：Get请求参数
        :param cookie：cookie参数
        :param header：header参数
        """
        response = requests.get(url=url, params=data, cookies=cookie, headers=header)
        return response

    def send_post(self, url, data, header=None, cookie=None):
        """
        Requests发送Post请求
        :param url：请求地址
        :param data：Post请求参数
        :param data：Post请求参数
        :param cookie：cookie参数
        :param header：header参数
        """
        response = requests.post(url=url, json=data, cookies=cookie, headers=header)
        return response

        # 主函数调用

    def run_main(self, method, url, data, header, cookie=None):
        try:
            result = ''
            if method.upper() == 'GET':
                result = self.send_get(url, data, header, cookie)
            elif method.upper() == 'POST':
                result = self.send_post(url, data, header, cookie)
            return result
        except Exception as e:
            logger.exception('请求主函数调用失败：{}'.format(e))


# 实例
baseRequest = BaseRequest()
