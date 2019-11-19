# -*- coding: utf-8 -*-
# @Time : 2019/11/13 9:36
# @Author : kira
# @Email : 262667641@qq.com
# @File : project_path.py
# @Project : risk_project

import os

# 根目录路径
base_path = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))  # D:\auto_test\risk_project

# 测试数据所在路径
data_path = os.path.join(base_path, "data", "risk_api.xlsx")

# 配置文件所在路径
conf_path = os.path.join(base_path, "config", "data_conf.ini")

# 测试报告所在路径
test_report = os.path.join(base_path, "OutPut", "reports")

# log 所在路径
log_path = os.path.join(base_path, "OutPut", "Log")

# 测试用例目录
test_case = os.path.join(base_path, "test_case")


if __name__ == '__main__':
    print("\n", base_path,
          "\n", test_report,
          "\n", conf_path,
          "\n", data_path)
