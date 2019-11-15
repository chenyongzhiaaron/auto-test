# -*- coding: utf-8 -*-
# @Time : 2019/11/13 14:51
# @Author : kira
# @Email : 262667641@qq.com
# @File : do_mysql.py
# @Project : risk_project

import pymysql.cursors
from common import project_path
from common.get_conf_data import GetConfigData

class DoMysql():

    def do_mysql(self, sql):
        # conf_path =project_path.conf_path
        # connect_message = eval(GetConfigData().get_config_data(conf_path, 'DB', "Mysql"))
        # connect_mysql = pymysql.connect(**connect_message)
        conn_mysql = pymysql.connect(
            host="129.204.136.250",
            port=3306,
            user="marketinfo",
            password="ryeKJIIeNcSCqklswE",
            db="user",
            charset='utf8mb4',
        )

        cus = conn_mysql.cursor(pymysql.cursors.DictCursor)     # 获取游标对象
        cus.execute(sql)
        res = cus.fetchone()
        cus.close()
        return res


if __name__ == '__main__':
    tt = DoMysql()
    print(tt.do_mysql("SELECT * FROM info;"))
