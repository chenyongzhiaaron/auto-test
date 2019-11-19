# -*- coding: utf-8 -*-
# @Time : 2019/11/13 14:51
# @Author : kira
# @Email : 262667641@qq.com
# @File : do_mysql.py
# @Project : risk_project

import pymysql.cursors
from common import project_path
from common.get_conf_data import GetConfigData

# ==================================== 读取配置文件 ====================================

db_path = project_path.conf_path
# config_db = GetConfigData().get_config_data(db_path, "MySQL", "mysql")
# config_db = eval(GetConfigData().get_config_data(db_path, 'DB', 'mysql'))
# config_db = eval(GetConfigData().get_config_data(db_path, 'DB_1', 'mysql'))
# print(config_db)
# print(type(config_db))
host = GetConfigData().get_config_data(db_path, "MySQL_test", "host")
port = GetConfigData().get_config_data(db_path, "MySQL_test", "port")
password = GetConfigData().get_config_data(db_path, "MySQL_test", "password")
database = GetConfigData().get_config_data(db_path, "MySQL_test", "database")
charset = GetConfigData().get_config_data(db_path, "MySQL_test", "charset")

# ==================================== 读取配置文件 =====================================
class DoMysql():

    def __init__(self, sql, method="insert"):

        '''
        初始化 mysql 链接属性
        :param sql:
        :param method: method in ("insert","delete","update","select")
        '''

        self.sql = sql
        self.method = method
        self.db_path = project_path.conf_path
        self.db_conn_message = eval(GetConfigData().get_config_data(self.db_path, "DB", "mysql"))
        # self.db_conn_message = eval(GetConfigData().get_config_data(db_path, "MySQL", "mysql"))

    def conn_mysql(self):
        '''
        连接 mysql
        :return: 返回连接实例
        '''
        conn_mysql = pymysql.connect(**self.db_conn_message)    # 传入字典，连接数据库
        return conn_mysql

    def do_mysql(self):
        """
        执行 mysql 数据库操作
        :return: 返回操作结果，以字典形式返回
        """
        conn = self.conn_mysql()                    # 获取连接实例
        result = None
        with conn.cursor() as cursor:
            if self.method == "insert":
                try:
                    cursor.execute(str(self.sql))   # 执行插入 sql 操作
                    conn.commit()                   # 提交事务
                    result = "插入成功"
                except Exception:
                    print("插入异常", Exception)
                    conn.rollback()                 # 异常回滚
                finally:
                    conn.close()                    # 关闭连接
            elif self.method == "delete":
                try:
                    cursor.execute(str(self.sql))   # 执行删除 sql
                    conn.commit()
                    result = "删除成功"
                except Exception:
                    print("删除异常", Exception)
                finally:
                    conn.close()
            elif self.method == "update":
                try:
                    cursor.execute(str(self.sql))   # 执行更新 sql
                    conn.commit()
                    result = "更新成功"
                except Exception:
                    print("更新异常", Exception)
                    conn.rollback()
                finally:
                    conn.close()
            else:
                cursor.execute(str(self.sql))       # 执行查询 sql
                result = cursor.fetchone()          # 返回一条查询结果
                conn.close()
        return result                               # 返回操作结果


if __name__ == '__main__':
    sql = "SELECT * FROM marketinfo.`user`;"
    method = "select"
    tt = DoMysql(sql,method)
    print(tt.do_mysql())
    # pass
