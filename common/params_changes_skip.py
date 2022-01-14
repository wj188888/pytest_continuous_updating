# -- coding:utf-8 --
'''
    pytest 使用 parametrize 参数化的时候，有多组测试数据，需要对其中的一些测试数据加标记跳过，可以用pytest.param实现。
'''

# pytest.param
# 先看下 pytest.param 源码,可以传三个参数
'''
param values ：按顺序传参数集值的变量args
keyword marks : marks关键字参数，要应用于此参数集的单个标记或标记列表。
keyword str id: id字符串关键字参数，测试用例的id属性
'''
# 例子
import pytest
# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/

@pytest.mark.parametrize("test_input,expected", [
    ("3+5", 8),
    pytest.param("6*9", 42, marks=pytest.mark.xfail),
])
def test_eval(test_input, expected):
    assert eval(test_input) == expected


@pytest.mark.parametrize("user,psw",
                         [("yoyo1", "123456"),
                          ("yoyo2", "123456"),
                          pytest.param("yoyo3", "123456", marks=pytest.mark.skip)])
def test_login(user, psw):
    print(user + " : " + psw)
    assert 1 == 1

@pytest.mark.parametrize("user,psw",
                         [pytest.param("wangjie1", "123456"),
                          pytest.param("wangjie2", "123456"),
                          pytest.param("wangjie3", "123456", marks=pytest.mark.skip)])
def test_login1(user, psw):
    print(user + " : " + psw)
    assert 1 == 1


# id参数是我们进行测试的时候的
@pytest.mark.parametrize("user,psw",
                         [pytest.param("yoyo1", "123456", id="test case1: yoyo1"),
                          pytest.param("yoyo2", "123456", id="test case2: yoyo2"),
                          pytest.param("yoyo3", "123456", marks=pytest.mark.skip, id="test case3: yoyo3")])
def test_login2(user, psw):
    print(user + " : " + psw)
    assert 1 == 1