#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
练习
小明身高1.75，体重80.5kg。请根据BMI公式（体重除以身高的平方）帮小明计算他的BMI指数，并根据BMI指数：

低于18.5：过轻
18.5-25：正常
25-28：过重
28-32：肥胖
高于32：严重肥胖
用if-elif判断并打印结果：

height = 1.75
weight = 80.5
'''

def checkfloat(num):
    try:
        if float(num)>0:
            return float(num)
        else:
            return False
    except ValueError as e:
        return False
    except KeyboardInterrupt as e:
        return False
#   finally
#   pass

def bmi(weight,height):
    bmi=weight/height**2
    if bmi>32:
        return '严重肥胖'
    elif bmi>28:
        return '肥胖'
    elif bmi>25:
        return '过重'
    elif bmi>18.5:
        return '正常'
    else:
        return '过轻'

def inputw():
    w=input('请输入小明的体重(kg)：')
    return checkfloat(w)
def inputh():
    h=input('请输入小明的身高(m)：')
    return checkfloat(h)

def main():
    print('======BMI公式（体重除以身高的平方）======')
    while True:
        w=inputw()
        h=inputh()
        if w and h:
            print('------\n小明体重'+str(w)+'kg，身高'+str(h)+'m')
            print('小明属于'+bmi(w,h)+'\n------')
        else:print('--\n有没有搞错\n--')
main()