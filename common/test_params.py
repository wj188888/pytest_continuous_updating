# -- coding:utf-8 --
import requests
import pytest

'''
   ！！！这个py没有成功 ！！！
'''
# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/
#
# 用例的id名称
names = ["login nam1", "login name2"]
# 测试数据 list of dict
test_data = [{
                "url": "http://49.235.x.x:5000/api/v1/login/",
                "method": "POST",
                "headers":
                    {
                        "Content-Type": "application/json"
                    },
                "json":
                    {
                        "username": "test",
                        "password": "123456"
                    }

        },
        {
            "url": "http://49.235.x.x:5000/api/v1/login/",
            "method": "POST",
            "headers":
                {
                    "Content-Type": "application/json"
                },
            "json":
                {
                    "username": "test",
                    "password": "123456"
                }

        }
        ]

#
def test_login(param):
    r = requests.session().request(**param)
    print(r.text)