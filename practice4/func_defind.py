# -*- coding: utf-8 -*-
# @Time : 2019/11/26 21:10
# @Author : lzm
# @Function : python函数和过程


"""
在python中使用def关键字定义一个过程或者一个函数
带有return返回值得是一个函数，不带有返回值的可以称之为过程
这里不是太明白，都是使用def定义的，唯一区别就是一个有返回值一个没有返回值，为什么是两个名称
个人依据java的理解是，即使没有带有返回值也可以称为函数，只是没有返回值得函数，或者说过程的返回值是None
"""


def process():
    """  函数描述，可以不写  """
    print("this is a process")


def func():
    print("this is a function")
    return 0


# 调用
process()
func()


