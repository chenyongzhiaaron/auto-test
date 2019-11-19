# -*- coding: utf-8 -*-
# @Time : 2019/11/14 16:34
# @Author : kira
# @Email : 262667641@qq.com
# @File : conn_mongo.py
# @Project : risk_api_project


import pymongo

"""
mongo里面表名备注
visitedInfoBean 轻松借
AdvanceVisitedInfoRecord 大王
easy_statistic+dt(线上库) statistics_dt(mongo正式库)

"""


class MongoDB():
    def __init__(self, db_name, table_name, dt):
        '''

        :param table_name:数据库名
        :param dt: 日期时间
        '''
        self.table_name = table_name
        self.dt = dt
        self.db_name = db_name

    def connect_mongo(self):
        '''
        mongo 库配置，
        :return:
        '''
        client = pymongo.MongoClient(host='', port='')  # 获取链接实例
        db = client[self.db_name]  # 链接数据库
        my_table = db[self.table_name + self.dt]  # 获取集合对象表的名称（）
        return my_table


if __name__ == '__main__':
    pass
