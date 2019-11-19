# -*- coding: utf-8 -*-
# @Time : 2019/11/19 14:29
# @Author : kira
# @Email : 262667641@qq.com
# @File : assert_dict.py
# @Project : risk_api_project

import json
import operator
from common.do_excel import DoeExcel


class AssertDict():
    def is_contain(self, expect_result, respone_result):
        '''

        :param str_one:
        :param str_two:
        :return:
        '''
        flag = None
        if expect_result.items() <= respone_result.items():
            flag = 1
        else:
            flag = 0
        return flag


    def extractDictAFromB(self, A, B):
        return dict(
            [
                (k, B[k]) for k in A.keys() if k in B.keys()
            ]
        )


if __name__ == '__main__':
    # first ={'data': {'user': {'id': 'kira', 'username': '测试人员账户'}}}
    first ={'id': 'kira'}
    # first ={'': ''}
    second = {'msg': '登陆成功', 'code': 200, 'data': {'user': {'id': ['kira', 'username', '测试人员账户'], 'orgName': None, 'type': None, 'province': None, 'city': None, 'area': None, 'createTime': '2019-11-18T17:59:18.000+0000', 'updateTime': '2019-11-18T18:00:47.000+0000'}, 'token': 'eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJraXJhIiwiZXhwIjoxNTc0MjM3Mzg5LCJvcmdOYW1lIjoib3JnTmFtZSJ9.7-YsEIyDiAUNzrVzNUm-TFysrHL0fLnKFdLQAX4czyY'}}
    test = AssertDict().is_contain(first, second)
    # print(test)
    test_1 = AssertDict().extractDictAFromB(first,second)
    print(test_1)
