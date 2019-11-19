# -*- coding: utf-8 -*-
# @Time : 2019/11/18 15:32
# @Author : kira
# @Email : 262667641@qq.com
# @File : run_main.py
# @Project : risk_api_project

import unittest
from common import project_path
from HTMLTestRunner import HTMLTestRunner
# from HTMLTestRunnerNew import HTMLTestRunner
from test_case import TestRiskApi

# 创建测试套件
suit = unittest.TestSuite()

# 创建测试用例加载器
loader = unittest.TestLoader()
# 加载测试用例
# test_case = suit.addTest(loader.loadTestsFromModule(TestRiskApi))
test_case = suit.addTest(loader.discover(project_path.test_case, pattern="Test*.py"))
fb = open(project_path.test_report + "/TestReport.html", "wb")

runner = HTMLTestRunner(stream=fb, verbosity=2, title="英大财险接口测试报告", description="英大财险所有接口进行接口自动化测试")
runner.run(suit)
