# -*- coding: utf-8 -*-
# @Time : 2019/11/26 22:20
# @Author : lzm
# @Function :  局部变量和全局变量

"""
在函数中定义的变量称为局部变量，局部变量的作用域只局限于当前函数
全局变量的作用域是整个程序，在函数中无法修改全局变量的值，除非使用global
当全局变量和局部变量重名时，在函数作用域中局部变量生效，在函数作用域之外，全局变量生效
"""


address = "北京"


def change_address () :
    address = "上海"
    print("address %s"%address)


change_address()
print(address)


print("----------分割线----------------")


def change_global () :
    global address
    address = "南京"
    print("change_global %s"%address)


print(address)
change_global()
print(address)


print("----------分割线----------------")


"""
不建议使用的一种方式，在方法体内创建全局变量，这样在方法调用多次之后，一旦出现异常，不好定位问题，代码规范问题
"""


def init_global_in_func():
    global name
    name = "张三"
    print(name)


init_global_in_func()
print(name)
