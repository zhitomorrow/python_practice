# -*- coding: utf-8 -*-
# @Time : 2019/11/26 21:20
# @Author : lzm
# @Function : 函数返回值

"""
函数的返回值：可以没有返回值，可以是数字、字符串、字典、列表，
可以是单独一个，也可以是使用都好隔开的多种类型，当返回值是使用逗号隔开的多个时，打印返回值显示的是一个元组
将函数返回值赋值给一个变量后，可以打印返回值
"""


def test1():
    return 1


def test2():
    return "str"


def test3():
    return ['1', '2', 'a']


def test4():
    return {"name": "lzm", "age": 28}


def test5():
    return 1, "asd", ["1", "2"], {"address": "北京"}


x = test1()
print(x)
y = test2()
print(y)
z = test3()
print(z)
a = test4()
print(a)
b = test5()
print(b)

