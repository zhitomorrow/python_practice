# -*- coding: utf-8 -*-
# @Time : 2019/11/19 21:37
# @Author : lzm
# @Function :  测试for循环

for i in range(0, 10, 2):
    if i == 6:
        break
    else:
        print("当前循环的位置是%s" % i)

# 循环时输出index值

for index, item in enumerate(range(1, 10)):
    print(index,item)