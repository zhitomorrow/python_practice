# -*- coding: utf-8 -*-
# @Time : 2019/11/19 22:16
# @Author : lzm
# @Function : 列表测试代码

names = ["Lay zhou", "Jackson", "Trump"]

# print(names)
'''
# add
names.append("Koeba")  # 添加到列表最后
print(names)

names.insert(1, "will")  # 添加到指定位置
print(names)

# update
names[2] = "Rose"
print(names)

# del
# names.pop()  # 默认删除最后一个
# print(names)

# names.pop(1)
# print(names)

# del names[1]
# print(names)


# search
print(names[0])
print(names[1:3])  # 顾头不顾尾，意思就是只包含前面下标所指的数据，不后面下标包含的元素
print(names[:2])  # 从0开始获取数据时，0可以不写

print(names[-1])  # 获取最后一个元素
print(names[-3:-1])  # 获取倒数3个元素，由于是从左往右数的，因此需要写-3 -1
print(names[:-2])  # 从最后一个开始，同样可以不写-1

# others

names.append("Rose")
print(names.count("Rose"))  # 统计元素出现的次数

names2 = [1, 2, 3, 4]
names.extend(names2)  # 合并两个列表，合并之后列表2还存在
print(names, names2)

# 删除变量
del names2
# print(names2)  # 异常

# copy

# names2 = names.copy()

# print(names2)

# names[1] = "Li"

# print(names,names2)

# 浅拷贝 列表中包含列表，拷贝子列表的地址
home = ["张三", ["balance", 2000]]
home2 = home.copy();
print(home2)

home[1][1] = 1000
print("home的值是", home)
print("home2的值是：", home)
'''
# copy的其他两种方式
print(names)
names3 = names[:]
print(names3)
names4 = list(names)
print(names4)


# 排序
# print(names)
# names.sort()
# print(names)


# 反转
# print(names)
# names.reverse()
# print(names)





