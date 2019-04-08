#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: insert_erase_splice_find.py
@time: 2019/4/8 23:10
@desc:第28讲:链表操作-插入、删除、查找和移动
"""

if __name__ == '__main__':
    L = [-2, -1, 1, 2]
    # 插入操作
    iter = 0
    while iter != len(L) and L[iter] < 0:
        iter += 1
    L.insert(iter, 0)
    print(L)
    # 删除操作
    iter = 0
    while iter != len(L):
        if L[iter] > 0:
            L.remove(L[iter])
        else:
            iter += 1
    print(L)
    # 移动操作
    X = [-5, -4, -3]
    # python在特定插入点扩展列表
    L[0:0] = X
    print(L)
    # 查找
    L.remove(0)
    print(L)