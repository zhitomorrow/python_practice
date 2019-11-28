# -*- coding: utf-8 -*-
# @Time : 2019/11/27 23:07
# @Author : lzm
# @Function :  文件操作


# 读取文件内的全部内容
def read_file():
    with open("application-aliyun.yml", "r", encoding="utf-8") as f:
        for line in f:
            print(line)


# 根据文件中定义的key值，查询对应的value值，如输入server，那么返回port:80，目前只支持一级目录查找
def search_file(*args):
    with open("application-aliyun.yml", "r", encoding="utf-8") as f:
        for index, line in enumerate(f.readlines()):
            if line.startswith(" "):
                continue
            else:
                if line.startswith(args[0]):
                    get_value_by_name(index+1)
                    break


temp = []


def get_value_by_name(*args):
    with open("application-aliyun.yml", "r", encoding="utf-8") as f:
        for line in f.readlines()[args[0]:]:
           if not line.startswith(" "):
               break
           temp.append(line)


# read_file()


# search_file("server")


str = input("请输入要查询的组件名称，输入all查看全部内容：")

if str == "all":
    read_file()
else:
    search_file(str)


print(temp)