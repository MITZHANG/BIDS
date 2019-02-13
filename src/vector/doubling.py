#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: doubling.py
@time: 2019/2/13 21:55
@desc: 第25讲:容量之妙-向量容量是高效的来源
"""

from common_lib.vector import Vector

if __name__ == '__main__':
    n = 40
    #size()返回当前元素个数, capacity()返回当前容量
    A = Vector()
    for i in range(n):
        print(A.size(), A.capacity())
        A.push_back(0)
    print(A.size(), A.capacity())

    B = Vector()
    # 提前预留容量n.
    B.resize(n)
    for i in range(n):
        print(B.size(), B.capacity())
        B.push_back(0)
    print(B.size(), B.capacity())