# -*- coding: utf-8 -*-
# @Time : 2019/11/20 22:46
# @Author : lzm
# @Function : 实现购物车功能，输入q直接退出程序

product_list = [("Iphone", 9999), ("Coffee", 20), ("Mac Pro", 25589)]

shopping_list = []
salary = input("Input your salary:")
if salary.isdigit():
    salary = int(salary)
    while True:
        for index, item in enumerate(product_list):
            print(index, item)
        user_choice = input("选择要买嘛？>>>:")
        if user_choice.isdigit():
            user_choice = int(user_choice)
            if user_choice  < len(product_list) and user_choice >= 0 :
                p_item = product_list[user_choice]
                if p_item[1] <= salary:  # 买的起
                    shopping_list.append(p_item)
                    salary -= p_item[1]
                    print("Added %s into shopping cart,your current balance is \033[31;1m%s\033[0m" %(p_item,salary) )
                else:
                    print("\033[41;1m你的余额只剩[%s]啦，还买个毛线\033[0m" % salary)
            else:
                print("product code [%s] is not exist!"% user_choice)
        elif user_choice == 'q':
            print("--------shopping list------")
            for p in shopping_list:
                print(p)
            print("Your current balance:",salary)
            exit()
        else:
            print("invalid option")