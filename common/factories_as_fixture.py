# -- coding:utf-8 --
# 工厂化的fixture
# 在一个测试用例中需要多次调用同一个fixture的时候，工厂化的 fixture 的模式对于一个 fixture 在单一的测试中需要被多次调用非常有用。
# 之前写fixture是直接return一个数据，在测试用例中可以直接使用，现在我们需要返回一个生成数据的函数，这样就能在用例中多次调用了

import pytest

# def test_customer_records(make_customer_record):
#     customer_1 = make_customer_record("Lisa")
#     customer_2 = make_customer_record("Mike")
#     customer_3 = make_customer_record("Meredith")
#     print(customer_1)
#     print(customer_2)
#     print(customer_3)

# 工厂化的fixture的场景用例
@pytest.fixture()
def register():

    def _register(user):
        # 调用注册接口，返回结果
        print("注册用户：%s" % user)
        result = {"code": 0, "message": "success"}
        return result

    return _register


def test_case_1(register):
    '''测试重复注册接口案例'''
    # 第一次调用注册
    result1 = register("yoyo")
    assert result1["message"] == "success"

    # 第二次调用
    result2 = register("yoyo")
    if result2:
        print(f"你已经注册了，{result2},请不要再次注册，请直接登录")

    # 真实场景可以断言 已被注册了