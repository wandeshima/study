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
print('BMI公式（体重除以身高的平方）')
while True:
    inputweight=input('请输入体重(kg)：')
    inputheight=input('请输入身高(m):')

    weight=float(inputweight)
    height=float(inputheight)

    bmi=weight/height**2
    
    print('小明')
    if bmi>32:
        print('严重肥胖')
    elif bmi>28:
        print('肥胖')
    elif bmi>25:
        print('过重')
    elif bmi>18.5:
        print('正常')
    else:
        print('过轻')
