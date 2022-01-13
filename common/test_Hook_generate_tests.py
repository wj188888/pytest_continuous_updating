# -- coding:utf-8 --
# Hook函数之参数化生成测试用例pytest_generate_tests
'''
    pytest 实现参数化有三种方式:
        pytest.fixture() 使用 fixture 传 params 参数实现参数化
        @pytest.mark.parametrize 允许在测试函数或类中定义多组参数，在用例中实现参数化
        pytest_generate_tests 允许定义自定义参数化方案或扩展
'''
# pytest_generate_tests 在测试用例参数化收集前调用此钩子函数，根据测试配置或定义测试函数的类或模块中指定的参数值生成测试用例，可以扩展和自定义
# 有时您可能想要实现自己的参数化方案或实现某种动态性来确定 fixture 的参数或范围
def test_valid_string(stringinput):
    assert stringinput.isalpha()
