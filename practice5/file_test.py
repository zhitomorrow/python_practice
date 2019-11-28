# -*- coding: utf-8 -*-
# @Time : 2019/11/28 22:48
# @Author : lzm
# @Function : file的tell和seek方法练习


with open("test.txt", "r", encoding="utf-8") as f:
    for index, line in enumerate(f.readlines()):
        print("行号[%s],内容[%s]" % (index, line))
        if line.startswith(" "):
            print("以空格开头")

    # print(f.readline())
    # print(f.tell())
    # print(f.readline())
    # print(f.tell())


# str = " 123 "
# print(str.startswith(" "))

