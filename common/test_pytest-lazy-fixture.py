# -- coding:utf-8 --
# 这一章就pytest-lazy-fixture插件的使用
# pytest-lazy-fixture 插件是为了解决测试用例中用 @pytest.mark.parametrize 参数化调用fixture的问题，先pip安装
# pip install pytest-lazy-fixture
import pytest

# @pytest.fixture(params=[1, 2])
# def one(request):
#     return request.param
#
#
# @pytest.mark.parametrize('arg1,arg2', [('val1', pytest.lazy_fixture('one')),])
# def test_func(arg1, arg2):
#     print(arg1, arg2)
#     assert arg2 in [1, 2]

# fixture参数化 params
# import pytest

@pytest.fixture
def one():
    return 1

@pytest.fixture
def two():
    return 2

@pytest.fixture(params=[
    pytest.lazy_fixture('one'),
    pytest.lazy_fixture('two')
])
def some(request):
    print(request.param)
    return request.param

def test_func(some):
    assert some in [1,2]