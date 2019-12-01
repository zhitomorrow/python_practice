# -*- coding: utf-8 -*-
# @Time : 2019/12/1 20:30
# @Author : lzm
# @Function : 简单生成器

# 列表
list1 = [x+2 for x in range(10)]
for i in list1:
    print("list1>>>%s" % i)
# 生成器
list2 = (x+2 for x in range(10))
for j in list2:
    print("list2>>>%s" % j)


