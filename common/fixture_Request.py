# -- coding:utf-8 --
'''
request 是 pytest的内置fixture
# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/
'''
# 第一部分：request.params
import pytest

# 测试数据
# test_data = ["user1", "user2"]
#
#
# @pytest.fixture(params=test_data)
# def register_users(request):
#      # 获取当前的测试数据,使用request.param去获取数据
#      user = request.param
#      print("\n拿着这个账号去注册：%s"%user)
#      result = "success"
#      return user, result
#
#
# def test_register(register_users):
#     user, result = register_users
#     print("在测试用例里面里面获取到当前测试数据：%s"%user)
#     print(result)
#     assert result == "success"

# 对上边内容进行解释，我们可以再fixture的函数进行参数化，但是不能在带有test_开头的用例中进行参数化；
# 用例里面用 request.param 却不能获取到测试的请求参数；

# ===================================================
# 第二部分：request.config
# 获取测试的配置文件参数，这个在前面讲命令行参数的时候有用到过.
# 在 conftest.py 写一个 hook函数， pytest_addoption 的作用是用于获取命令行参数，request.config 用于读取测试的配置数据
def test_answer_1(request):
    type = request.config.getoption("--cmdopt")
    print("获取到命令行参数：%s" % type)


def test_answer_2(cmdopt):
    print("获取到命令行参数：%s" % cmdopt)

# 第三部分：request.module
# smtpserver = "mail.python.org"
#
# def test_showhelo(smtp):
#
#     print("case showhelo")

# pytestconfig 的作用跟 request.config 是一样的，都是获取配置对象
# log_cli 是控制台实时输出日志，可以设置True 和 False，也可以设置1 和 0，默认是关闭状态（False）
# 当 log_cli = 0 或默认的 False 状态时，命令行输入 pytest 运行用例，在控制台输出是按每个模块显示运行结果,就是把一个.py文件的内容，把每个测试用例都显示出来；
