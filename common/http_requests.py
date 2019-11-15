# -*- coding: utf-8 -*-
# @Time : 2019/11/13 14:06
# @Author : kira
# @Email : 262667641@qq.com
# @File : http_requests.py
# @Project : risk_project

import requests
import logging


class HttpRequests():

    def http_requests(self, method, url, params=None, header=None):
        '''
        封装发送 http 请求
        :param method: 请求方法
        :param url: 请求地址
        :param params: 请求参数，默认不传
        :param header: 请求 header ，默认不传
        :return: 返回请求结果
        '''
        res = None
        if method == 'post':
            res = requests.post(url=url, data=params, headers=header)
        elif method == "get":
            res = requests.get(url=url, params=params, headers=header)
        elif method == 'put':
            res = requests.put(url=url, data=params, headers=header)
        return res


if __name__ == '__main__':
    url = "http://129.204.178.29:9527/api/orgTree"

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
    print(response.json())
