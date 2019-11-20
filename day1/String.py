# -*- coding: utf-8 -*-
# @Time : 2019/11/20 22:12
# @Author : lzm
# @Function : 测试字符串的各个方法

print("asdfasdf".count("a", 2, 5))  # 计算从下标值为2的地方开始到下标值为5的地方结束，a出现的次数
print("asdfggg".capitalize())  # 首字母大写
print("ASDf".casefold())  # 大写转换为小写，类似于lower方法
print("asf".center(20, "*"))  # 20个字符，不够的使用*补全，字符串显示在中间
print("asdfg".endswith("g"))
print("asdf\tgg".expandtabs(tabsize=1))  # 使用一个空格代替\t
name = "my \tname is {name} and i am {year} old"
print(name[name.find("name"):])  # 字符串分片，以name的位置开始到结束
print(name.format(name="aa", year=22))  # 字符串格式化
print(name.format_map({"name": "ss", "year": 2}))  # 以map的格式传入参数
print("0".isdigit())  # 是否是整数，不包含负数
print("33A".isnumeric())  # 是否是数字，不包含16进制
print(",".join(["1", "2", "3"]))  # 拼接字符串
print("asd".upper())
print("ASD".lower())
print("  asd\n".strip())  # 前后去空格，左右去空格是lstrip  和  rstrip
print("asdFG".swapcase())  # 大小写转换
print("----")
