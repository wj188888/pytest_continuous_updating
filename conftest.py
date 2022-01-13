# -- coding:utf-8 --
import pytest

@pytest.fixture(autouse=True)
def get_ini(pytestconfig):
    '''读取ini配置信息'''
    # 读取 log_cli配置
    log_cli = pytestconfig.getini('log_cli')
    print("获取到markers ：%s" % log_cli)
    addopts = pytestconfig.getini('addopts')
    print("获取到addopts的配置：%s " % addopts)