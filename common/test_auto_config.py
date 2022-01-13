# -- coding:utf-8 --
import pytest

# 有一些配置参数希望能加到配置里面，如configid, productid,以及测试环境的base_url地址，和账号相关信息。
# 动态添加配置信息:
'''
    adddini里面参数说明:
        第一个'url' 是参数的名称
        type 是类型，默认None，可以设置：None, "pathlist", "args", "linelist", "bool"
        default 是设置的默认值
        help 是设置帮助文档，方便查阅
'''
def test_h(home_url):
    print("用例：%s" % home_url)