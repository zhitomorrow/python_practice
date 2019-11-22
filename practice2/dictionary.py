# -*- coding: utf-8 -*-
# @Time : 2019/11/22 21:47
# @Author : lzm
# @Function : 练习字典的常用方法


'''
字典是无序的
key必须是唯一的，所以天生去重
key-value形式，类似于java中的Map
'''

area = {
    "北京": {
        "朝阳区": [],
        "海淀区": [],
        "昌平区": ["天通苑", "沙河"],
        "密云区": []
    },
    "河南": {
        "洛阳市": ["新安县", "偃师县"],
        "郑州市": [],
        "驻马店": []
    }
}

# 查找
print(area.get("北京"))
print(area.get("北京").get("昌平区"))
# 使用get方法，如果key值不存在，那么返回None，不会出现异常，使用area[]的方法如果查找不存在的key值会抛出异常


# 新增
area["北京"]["朝阳区"] = ["朝阳体育中心", "北京东站"]
print(area)

# 修改
area["河南"]["洛阳市"] = ["新安县", "偃师县", "孟津县"]
print(area)

# 删除
area["北京"].pop("密云区")  # 常用删除方法
print(area)

# 也可以使用del删除
del area["北京"]["海淀区"]
print(area)

# 其他操作
area.setdefault("天津", {"武清": {}})
# 如果天津不存在，那么使用默认值创建，如果存在，那么不做任何操作
print(area)

# 字典转列表
print(area.items())

# update 将其他字典的值更新到area中
b = {"test": "1", "t2": "2"}
area.update(b)
print(area)

# 遍历字典
# for i in area:
#     print(i)

# 循环的另外一种写法
# 不推荐使用这种写法，会发生转换，影响效率
# for k, v in area:
#     print(k, v)


