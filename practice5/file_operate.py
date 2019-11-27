# -*- coding: utf-8 -*-
# @Time : 2019/11/27 23:07
# @Author : lzm
# @Function :  文件操作，实现增删改查


# 读取文件内的全部内容
def read_file():
    with open("application-aliyun.yml", "r", encoding="utf-8") as f:
        for line in f:
            print(line)


# 根据文件中定义的key值，查询对应的value值，如输入server，那么返回port:80
def search_file(my_input):
    str = ""
    with open("application-aliyun.yml", "r", encoding="utf-8") as f:
        for line in f:
            if line.startswith(" "):
                continue
            else:
                if line.startswith(my_input):
                    str = get_value_by_name(f.tell())
                    break
    return str


temp = ""


def get_value_by_name(tell):
    with open("application-aliyun.yml", "r", encoding="utf-8") as f:
        f.seek(tell)
        line = f.readline()
        print(line)
        temp.append(line+",")
        if line.startswith(" "):
            get_value_by_name(f.tell())
        return temp


# read_file()


# search_file("server")


def test():
    with open("application-aliyun.yml", "r", encoding="utf-8") as f:
        for line in f:
            print(f.readline())
            print(f.tell())


test()
