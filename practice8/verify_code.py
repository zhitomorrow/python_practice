# -*- coding: utf-8 -*-
# @Time : 2019/12/3 23:04
# @Author : lzm
# @Function : 使用random模块生成6位数验证码


import random


def create_verify_code():
    code = ""
    for i in range(6):
        current = random.randrange(0, 6)
        if current == i:
            tmp = chr(random.randint(65, 90))
        else:
            tmp = random.randint(0, 9)
        code += str(tmp)
    return code


print(create_verify_code())
