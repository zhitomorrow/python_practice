# -*- coding: utf-8 -*-
# @Time : 2019/11/30 20:18
# @Author : lzm
# @Function : 嵌套函数测试


"""
嵌套函数：在一个函数内部，使用def关键字重新定义一个函数
嵌套函数类似于局部变量，作用域只能是处于外层函数内部，在外层函数外部是无法调用内部的嵌套函数的
"""

x = 0


def outter():
    print("this is outter,x=%s" % x)

    def inner():
        x = 1
        print("this is inner,x=%s" % x)
    inner()


outter()
