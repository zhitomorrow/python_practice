# -*- coding: utf-8 -*-
# @Time : 2019/12/1 20:34
# @Author : lzm
# @Function : 函数生成器


def func(x):
    my_num = x*2+1
    # print(my_num)
    yield my_num


"""
生成器，当取出最后一个值之后，如果继续调用next方法，那么就会抛出StopIteration异常，需要使用try...except捕获异常处理
或者使用for循环的方式获取生成器中的数据
"""


# try:
#     num = func(10)
#     num.__next__()
#     num.__next__()
# except Exception as err:
#     print(err)


for k in func(11):
    print(k)
