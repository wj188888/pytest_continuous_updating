# -- coding:utf-8 --
import pytest

# 在 conftest.py 写一个 hook函数， pytest_addoption 的作用是用于获取命令行参数，request.config 用于读取测试的配置数据
def pytest_addoption(parser):
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )

@pytest.fixture
def cmdopt(request):
    return request.config.getoption("--cmdopt")

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
@pytest.fixture(autouse=True)
def print_request(request):
    print("\n=======================request start=================================")
    print(request.module)
    print(request.function)
    print(request.cls)
    print(request.fspath)
    print(request.fixturenames)
    print(request.fixturename)
    print(request.scope)
    print("\n=======================request end=================================")

# 第五部分：pytestconfig
@pytest.fixture(autouse=True)
def get_ini(pytestconfig):
    '''读取ini配置信息'''
    # 读取 log_cli配置
    # log_cli = pytestconfig.getini('log_cli')
    # print("获取到markers ：%s" % log_cli)
    addopts = pytestconfig.getini('addopts')
    print("获取到addopts的配置：%s " % addopts)