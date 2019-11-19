# -*- coding: utf-8 -*-
# @Time : 2019/11/13 14:32
# @Author : kira
# @Email : 262667641@qq.com
# @File : get_conf_data.py
# @Project : risk_project

from configparser import ConfigParser
from common import project_path


class GetConfigData():

    def get_config_data(self, file_name, section, option):
        '''
        读取配置文件
        :param file_name:   配置文件路径
        :param section:     文件 section
        :param option:      文件 option
        :return:
        '''
        cf = ConfigParser()
        cf.read(file_name)
        value = cf.get(section, option)
        return value


if __name__ == '__main__':
    file_name = project_path.conf_path
    print(file_name)
    res = GetConfigData().get_config_data(file_name, 'CASE', 'sheet_list')
    res_1 = GetConfigData().get_config_data(file_name, 'DB', 'mysql')
    print(type(res))
    print(res)
    print(type(eval(res)))
    # print(eval(res))
