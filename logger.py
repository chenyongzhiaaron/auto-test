# -*- coding: utf-8 -*-
# @Time : 2019/11/18 10:17
# @Author : kira
# @Email : 262667641@qq.com
# @File : logger.py.py
# @Project : risk_api_project


import logging
from logging.handlers import RotatingFileHandler
import time
from common import project_path

fmt = "%(asctime)s-%(levelname)s-%(filename)s-[ line:%(lineno)d ] - 日志信息:%(message)s"
datefmt = "%Y-%m-%d- %H:%M:%S"
handler_1 = logging.StreamHandler()
current_time =time.strftime("%Y%m%d %H%M%S", time.localtime())
handler_2 =RotatingFileHandler(project_path.log_path+"/risk_api_{0}.log".format(current_time), backupCount=20, encoding="utf-8")

# 设置 rootlogger 的输出形式,输出内容
logging.basicConfig(format=fmt, datefmt=datefmt, level=logging.INFO, handlers=[handler_1, handler_2])


if __name__ == '__main__':
    logging.error("hhh")
    logging.info("12314")