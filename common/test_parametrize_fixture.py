# -- coding:utf-8 --
'''
    测试用例参数化的时候，使用 pytest.mark.parametrize 参数化传测试数据，如果我们想引用前面不同fixture返回的数据当测试用例的入参。
    可以用fixture 参数化 prams 来间接解决这个问题
    解决方案:
    request.getfixturevalue(“fixture name”) 方法来获取fixture的返回值
'''
# getfixturevalue 的作用是获取 fixture 的返回值
import pytest

@pytest.fixture
def a():
    return 'a'

@pytest.fixture
def b():
    return 'b'

@pytest.fixture(params=['a','b'])
def arg(request):
    return request.getfixturevalue(request.param)

def test_foo(arg):
    assert len(arg) == 1

# 实例场景
# web自动化的时候，想在 chrome 和 firefox 浏览器上测试同一功能的测试用例，对selenium还是蛮有用的
# 另外一个解决方案，使用 pytest-lazy-fixture 插件解决
import pytest
from selenium import webdriver

@pytest.fixture
def chrome():
    driver = webdriver.Chrome()
    yield driver
    driver.quit()

@pytest.fixture
def firefox():
    driver = webdriver.Firefox()
    yield driver
    driver.quit()

@pytest.fixture(params=['chrome', 'firefox'])
def driver(request):
    '''启动浏览器参数化,关键词getfixturevalue'''
    return request.getfixturevalue(request.param)

def test_foo1(driver):
    '''测试用例'''
    driver.get("https://www.baidu.com/")