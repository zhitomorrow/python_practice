# -*- coding: utf-8 -*-
# @Time : 2019/11/22 22:21
# @Author : lzm
# @Function :  集合测试

# 将一个列表转换成集合
list_1 = [0, 1, 3, 5, 7, 9]
list_1 = set(list_1)
print(list_1)

list_2 = set([0, 2, 4, 6, 8, 10])

# 交集
print(list_1.intersection(list_2))
print(list_1 & list_2)

# 并集
print(list_1.union(list_2))
print(list_1 | list_2)

# 差集： 在A集合中，但是不在B集合中
print(list_1.difference(list_2))
print(list_1 - list_2)

# 是否是子集
list_3 = set([3, 5, 7])
print(list_3.issubset(list_1))
# 是否是父集
print(list_3.issuperset(list_1))

# 对称差集 = AB的并集-AB的交集
print(list_1.symmetric_difference(list_2))
print(list_1 ^ list_2)


# AB集合没有任何交集，那么返回值为True，否则为False
list_4 = set([2, 6, 8])
print(list_3.isdisjoint(list_4))  # True
print(list_3.isdisjoint(list_1))  # False

# add
list_1.add(2)
print(list_1)

# update
list_1.update([888, 777, 666])
print(list_1)

# 删除，不返回任何值
list_1.discard(888)
print(list_1)






