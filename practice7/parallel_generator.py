# -*- coding: utf-8 -*-
# @Time : 2019/12/1 20:44
# @Author : lzm
# @Function : 斜程是比线程更小的单元，使用生成器实现协程的概念


import time


def consumer(name):
    print("%s 准备吃包子啦!" %name)
    while True:
        baozi = yield

        print("包子[%s]来了,被[%s]吃了!" %(baozi,name))


c = consumer("李四")
c.__next__()

# b1= "韭菜馅"
# c.send(b1)
# c.__next__()


def producer(name):
    c = consumer('A')
    c2 = consumer('B')
    c.__next__()
    c2.__next__()
    print("老子开始准备做包子啦!")
    for i in range(10):
        time.sleep(1)
        print("做了1个包子,分两半!")
        c.send(i)
        c2.send(i)


producer("张三")
