# -- coding:utf-8 --
from selenium import webdriver
import pytest
import time
# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/


@pytest.fixture(scope="module")
def open_broswer():
    '''打开浏览器'''
    driver = webdriver.Chrome()
    yield driver
    driver.close()


def test_blog(open_broswer):
    '''打开我的blog: https://www.cnblogs.com/yoyoketang/'''
    open_broswer.get("https://www.cnblogs.com/yoyoketang/")
    time.sleep(3)

# 对open_broswer使用不习惯，重命名这个函数：fixture里面的name参数
# 只需要把
# @pytest.fixture(scope="module")修改成下方的就可以了
# @pytest.fixture(scope="module", name="driver")
