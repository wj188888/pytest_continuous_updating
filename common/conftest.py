# -- coding:utf-8 --
import pytest

# 在 conftest.py 写一个 hook函数， pytest_addoption 的作用是用于获取命令行参数，request.config 用于读取测试的配置数据
def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )
    # 添加参数到pytest.ini，这是对pyest.ini的url进行添加
    parser.addini('url', type=None, default="http://49.235.92.12:8200/", help='添加 url 访问地址参数')
    '''解释上一行代码；
        type参数的几种类型：
            默认是：None
            还有其他的选项None, "pathlist", "args", "linelist", "bool"
            AAA:    type=None 默认读的是字符串
            AAA:    type="pathlist" 可以设置多个路径，会自动拼接ini文件这一层目录
            AAA:    type="args" 多个参数
            AAA:    type="linelist" 可以是多个命令行参数
            AAA:    type="bool" bool值，设置1或0
    '''
@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

# 获取 pytest.ini 配置参数;如果某一天我们的测试环境变了，这个时候不需要去改代码，只需在pytest.ini配置一个环境地址
'''
# pytest.ini配置文件
[pytest]

url = https://www.cnblogs.com/yoyoketang/
'''
@pytest.fixture(scope="session")
def home_url(pytestconfig):
    url = pytestconfig.getini('url')
    print("\n读取到配置文件的url地址：%s" % url)
    return url
# request.module
# @pytest.fixture(scope="module")
# def smtp(request):
#     server = getattr(request.module, "smtpserver", "smtp.qq.com")
#     print("fixture 获取到的server :%s" %server)
#     smtp = smtplib.SMTP(server, 587, timeout=5)
#     yield smtp
#     print("完成 %s (%s)" % (smtp, server))
#     smtp.close()

# 第四部分：request的相关成员对象
# @pytest.fixture(autouse=True)
# def print_request(request):
#     print("\n=======================request start=================================")
#     print(request.module)
#     print(request.function)
#     print(request.cls)
#     print(request.fspath)
#     print(request.fixturenames)
#     print(request.fixturename)
#     print(request.scope)
#     print("\n=======================request end=================================")

# 第五部分：pytestconfig
@pytest.fixture(autouse=True)
def get_ini(pytestconfig):
    '''读取ini配置信息'''
    # 读取 log_cli配置
    # log_cli = pytestconfig.getini('log_cli')
    # print("获取到markers ：%s" % log_cli)
    addopts = pytestconfig.getini('addopts')
    print("获取到addopts的配置：%s " % addopts)

# 读取项目的根目录
import os

import pytest
# import yaml
# 作者-上海悠悠 QQ交流群:717225969
# blog地址 https://www.cnblogs.com/yoyoketang/

#
# @pytest.fixture(scope="session", autouse=True)
# def dbinfo(request):
#     dbfile = os.path.join(request.config.rootdir,
#                         "config",
#                         "dbenv.yml")
#     print("dbinfo file path :%s" % dbfile)
#     with open(dbfile) as f:
#         dbenv_config = yaml.load(f.read(), Loader=yaml.SafeLoader)
#     print(dbenv_config)
#     return dbenv_config

# 工厂化的fixture
@pytest.fixture
def make_customer_record():
    created_records = []
    def _make_customer_record(name):
        record = {"name": name, "order": [1,2,3,4,5]}
        created_records.append(record)
        return record
    yield _make_customer_record

    for record in created_records:
        record

# 其中包含命令行选项和测试函数的参数化，向pytest.ini添加一个参数
# def pytest_addoption1(parser):
#     parser.addoption(
#         "--stringinput",
#         action="append",
#         default=[],
#         help="list of stringinputs to pass to test functions",
#     )

# def pytest_generate_tests(metafunc):
#     if "stringinput" in metafunc.fixturenames:
#         metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))


def pytest_generate_tests(metafunc):
    """ generate (multiple) parametrized calls to a test function."""
    if "param" in metafunc.fixturenames:
        metafunc.parametrize("param",
                             metafunc.module.test_data,
                             ids=metafunc.module.names,
                             scope="function")