# -*- coding: utf-8 -*-
# @Time : 2019/11/30 20:40
# @Author : lzm
# @Function :  装饰器实现

import time

"""
模拟java的AOP，给函数添加执行时间的功能
"""


# 装饰器函数
def timer(func):
    def decode():
        start_time = time.time()
        func()
        end_time = time.time()
        print("the func's run time is %s" % (end_time-start_time))
    return decode


"""
装饰器函数添加参数，当被装饰的函数存在参数时，timer装饰器因为没有参数，就会抛出异常，可以将*args和**kwargs传递给decode，
此时就可以兼容没有参数以及多个参数的情况
"""


def timer1(func):
    def decode(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        print("the func's run time is %s" % (end_time-start_time))
    return decode


"""
使用装饰器装饰带有返回值的函数：
上面的两个装饰器都只能处理没有带有返回值的函数，如果函数带有返回值，那么需要处理返回值问题
"""


def timer2(func):
    def decode(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("the func's run time is %s" % (end_time-start_time))
        return res
    return decode



# @timer
@timer1
def func1():
    time.sleep(3)  # 暂停3秒
    print("this is func1")


# @timer
@timer1
def func2():
    time.sleep(3)
    print("this is func2")


@timer1
def func3(name, age):
    time.sleep(1)
    print("name=%s,age=%s" % (name, age))


"""
python提供以下的语法糖：直接在被装饰的函数上添加注解，注解的名称即为装饰器函数的名称，如本例中的@timer
如被装饰的函数是func1，那么@timer注解等价于 func1 = timer(func1)
func1 = timer(func1)  ==>  func1 = decode  ,也就是说，通过嵌套函数执行被装饰函数且添加新的功能，通过高阶函数返回嵌套函数的引用，并且赋值给被装饰函数，以此来实现AOP功能

"""

"""
# func1 = timer(func1)
func1()
# func2 = timer(func2)
func2()
func3("lzm", 20)
"""


@timer2
def func4():
    print("this is func4")
    return "func test"


func4()









