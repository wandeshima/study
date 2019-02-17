#!/usr/bin/env python3
# -*- coding:utf-8 -*-

'''
练习
请使用迭代查找一个list中最小和最大值，并返回一个tuple：
'''

def findMinAndMax(L):
    if L==[]:
        return (None,None)
    else:
        min=L[0]
        max=L[0]
        for x in L:
            if x>min:
                min=min
            else:
                min=x
            if x<max:
                max=max
            else:
                max=x
        return (min,max)

def main():
    # 测试
    if findMinAndMax([]) != (None, None):
        print('测试失败!')
    elif findMinAndMax([7]) != (7, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1]) != (1, 7):
        print('测试失败!')
    elif findMinAndMax([7, 1, 3, 9, 5]) != (1, 9):
        print('测试失败!')
    else:
        print('测试成功!')
main()