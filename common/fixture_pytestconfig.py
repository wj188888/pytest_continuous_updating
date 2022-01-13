# -- coding:utf-8 --
# request 是pytest的一个内置 fixture ，作用是获取测试的上下文，可以通过request.config 获取配置对象。
# pytestconfig 的作用跟 request.config 是一样的，都是获取配置对象

# .getoption() 获取命令行参数
# .getini() 获取ini配置文件的参数

'''getini() 从 pytest.ini 配置文件获取参数'''