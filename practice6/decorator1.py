# -*- coding: utf-8 -*-
# @Time : 2019/11/30 21:25
# @Author : lzm
# @Function : 给装饰器函数传递参数

"""
给装饰器函数传递参数，根据传递的参数的不同，给被装饰函数添加不同的功能
"""


def auth(auth_type):
    def wrapper(func):
        def decode(*args, **kwargs):
            if auth_type == "1":
                print("this is auth_type_1")
            elif auth_type == "2":
                print("this is auth_type_1")
            else:
                 print("this is default auth_type")
            res = func(*args, **kwargs)
            return res
        return decode
    return wrapper


@auth(auth_type="1")
def test1():
    print("this is test1")


@auth(auth_type="2")
def test2():
    print("this is test2")


@auth(auth_type="3")
def test3():
    print("this is test3")


test1()
test2()
test3()



