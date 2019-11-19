# -*- coding: utf-8 -*-
# @Time : 2019/11/18 11:18
# @Author : kira
# @Email : 262667641@qq.com
# @File : run_main.py
# @Project : risk_api_project

import unittest
import logging
import json
import ddt
from ddt import ddt, data
from common import logger
from common.get_conf_data import GetConfigData
from common import project_path
from common.do_excel import DoeExcel
from common.http_requests import HttpRequests
from common.assert_dict import AssertDict

file_name = project_path.data_path
test_case = DoeExcel().do_excel(file_name)


@ddt
class TestRiskApi(unittest.TestCase):
    """ceshi"""

    def setUp(self):
        pass

    def tearDown(self):
        print("接口响应时间{}".format(self.respone_time))
        print(self.result)

    @data(*test_case)
    def test_risk_api(self, item):
        ''''''
        res = HttpRequests().http_requests(item["Method"], item["Url"], json=eval(item["Params"]),
                                           header=eval(item["Headers"]))
        self.result = res.json()  # 响应结果以 json 形式解释
        # respone_result = json.loads(self.result)  # 将响应结果由 json 转化为 dict
        test_result = None  # 定义测试结果为 None
        self.respone_time = res.elapsed.total_seconds()  # 记录接口响应时间
        logging.info(
            "正在进行{0}接口请求，执行第{1}条用例，请求的内容是{2}，请求url是{3}，请求header是{4}，请求参数是{5}".format(item["Module"], item["Id"],
                                                                                     item["Description"], item["Url"],
                                                                                     item["Headers"], item["Params"]))
        try:
            self.assertTrue(AssertDict().is_contain(eval(item["ExpectedResult"]), self.result),True)  # 断言是否为真
            test_result = 'PASS'
        except Exception as e:
            logging.error("请求出错，结果为{0}，请求参数为{1}".format(e, eval(item["Params"])))
            test_result = "FAULT"
        finally:
            DoeExcel().write_back(file_name, item["sheet_name"], item["Id"], str(self.result), test_result)
            logging.info("已执行写回 excel 操作")


if __name__ == '__main__':
    unittest.main()
