#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: array_and_vector.py
@time: 2019/2/9 13:33
@desc: 数组和向量
"""

from common_lib.vector import Vector

if __name__ == '__main__':

    n = 42
    c = 1

    # 定义
    V1 = Vector(n)

    # 初始化
    A1 = [c for i in range(n)]
    V2 = Vector(n, c)

    # 列表初始化
    V3 = Vector([1, 2, 3, 4, 5])
    for _, v in enumerate(V3):
        print(v, end=" ")
    print()

    # 动态变化
    V3.push_back(6)
    print(len(V3))
    print(V3.front(), V3.back())
    V3.pop_back()
    print(len(V3))
    print(V3.front(), V3.back())

    # 迭代器
    for _, v in enumerate(V3):
        print(v, end=" ")
    print()

