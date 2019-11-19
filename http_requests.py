# -*- coding: utf-8 -*-
# @Time : 2019/11/13 14:06
# @Author : kira
# @Email : 262667641@qq.com
# @File : http_requests.py
# @Project : risk_project

import requests
from common import project_path
from common.get_conf_data import GetConfigData
from common import logger
import logging

class HttpRequests():

    def http_requests(self, method, params_url, params=None, json=None, header=None):
        '''
        封装发送 http 请求
        :param method: 请求方法
        :param url: 请求地址
        :param params: 请求参数，默认不传
        :param header: 请求 header ，默认不传
        :param json:   请求 参数，json 格式
        :return: 返回请求结果
        '''
        base_url = eval(GetConfigData().get_config_data(project_path.conf_path, "URL", "url"))
        url = base_url + params_url
        res = None
        if method.lower() == 'post':
            try:
                res = requests.post(url=url, data=params, json=json, headers=header, verify=False, timeout=15)
                logging.info("正在进行 HTTP 请求，请求方式 post ")
            except Exception as e:
                logging.error("post 请求异常，错误是{0}，请求参数是{1}".format(e, json))
        elif method == "get":
            try:
                res = requests.get(url=url, params=params, headers=header, verify=False, timeout=15)
                logging.info("正在进行 HTTP 请求，请求方式 get ")
            except Exception as e:
                logging.error("get 请求异常，错误是{0}，请求参数是{1}".format(e, json))
        elif method == 'put':
            try:
                res = requests.put(url=url, data=params, headers=header, verify=False, timeout=15)
                logging.info("正在进行 HTTP 请求，请求方式 put ")
            except Exception as e:
                logging.error("put 请求异常，错误是{0}，请求参数是{1}".format(e, json))
        return res


if __name__ == '__main__':
    url = "/api/orgTree"

    headers = {
        'Content-Type': "application/json",
        'Authorization': "Bearer eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJraXJhIiwiZXhwIjoxNTczMDI5NTIwLCJvcmdOYW1lIjoib3JnTmFtZSJ9.zpx19C56wLJIdfUwOogjV7xpX5HuKnt7Zvpf6wlOMeo",
        'User-Agent': "PostmanRuntime/7.19.0",
        'Accept': "*/*",
        'Cache-Control': "no-cache",
        'Postman-Token': "b01346cf-0cd7-472a-9533-98d56c3e755f,4d6f9bef-caa3-4efe-ad68-f537f2aa3d5f",
        'Host': "129.204.178.29:9527",
        'Accept-Encoding': "gzip, deflate",
        'Cookie': "csrftoken=39T86elB3aL9gs3ul47Ea41B3RqBJo4lGXZtVlA0OQRSPTvk85kyTlv14C43MHQX",
        'Connection': "keep-alive",
        'cache-control': "no-cache"
    }

    response = HttpRequests().http_requests("get", url, header=headers)
    print(response.request.body)
    print(response.request.headers)
    print(response.json())
