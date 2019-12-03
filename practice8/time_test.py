# -*- coding: utf-8 -*-
# @Time : 2019/12/3 22:12
# @Author : lzm
# @Function : time模块练习

import time
from datetime import datetime
from datetime import timedelta  # 从datetime中引入timedelta


"""
时间的三种格式：
    1.时间戳
    2.格式化时间
    3.以元组的形势表示时间
"""

# 使用help方法查看time模块下的方法
# help(time)

# asctime([tuple])->string，传入一个元组，转换成一个字符串格式的日期，如果不传参数则默认为当前时间
print(time.asctime())   # Tue Dec  3 22:21:02 2019

# ctime(seconds)->string  将时间戳转换成字符串格式的日期,不传参数表示当前时间
print(time.ctime())  # Tue Dec  3 22:22:10 2019

# gmtime(seconds)->(tm_year, tm_mon, tm_mday, tm_hour, tm_min,
#                                tm_sec, tm_wday, tm_yday, tm_isdst)
x = time.gmtime()
print(x)
"""
time.struct_time(tm_year=2019, tm_mon=12, tm_mday=3, tm_hour=14, tm_min=24, tm_sec=33,
  tm_wday=1, tm_yday=337, tm_isdst=0)
"""
print(x.tm_year)  # 2019

# localtime(seconds)->将一个时间戳转换成本地时间，如果不传参数表示当前时间
"""
time.struct_time(tm_year=1973, tm_mon=11, tm_mday=30, tm_hour=5,
 tm_min=24, tm_sec=16, tm_wday=4, tm_yday=334, tm_isdst=0)
"""
print(time.localtime(123456256))


# mktime(tuple)—> 浮点数  ，将一个元组转换成一个时间戳
y = time.mktime(time.gmtime())
print(y)  # 1575354732.0

# 程序暂停
# time.sleep(2)  # 单位是秒

# 格式化日期，将一个元组日期格式化
z = time.strftime('%Y-%m-%d %H:%M:%S', x)
print(z)

# 字符串转换为日期元组
k = time.strptime('2019-12-03 14:35:13', '%Y-%m-%d %H:%M:%S')
print(k)


# 获取当前时间的时间戳
print(time.time())


"""
测试datetime的相关方法
"""

print("当前时间：%s" % (datetime.now()))

# 当前时间向前+3天
print(datetime.now()+timedelta(days=3))



