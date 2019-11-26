# -*- coding: utf-8 -*-
# @Time : 2019/11/26 21:54
# @Author : lzm
# @Function : 函数的调用顺序


"""
函数的调用顺序是自上而下的，如果函数的调用早于函数的定义，那么就会出现找不到函数的异常
"""


def t1():
    print("func_t1")
    t2()


# t1()  # 异常，NameError: name 't2' is not defined


def t2():
    print("func_t2")


t1()  # 正常

