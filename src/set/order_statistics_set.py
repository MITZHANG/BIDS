#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: order_statistics_set.py
@time: 2019/2/9 19:03
@desc: 第13讲：集合中的次序统计量-寻找集合中第k小的元素
"""

from common_lib.set import Set
from common_lib.vector import Vector

if __name__ == '__main__':
    S = Set([3, 2, 1, 4, 5])
    k = int(input("请输入k: "))
    if k<=0 or k > S.size():
        print("超出范围！")
    else:
        # 第一种方法
        print(sorted(S.copy())[k-1])
        # 第二种方法
        V = Vector(k-1)
        for i in range(0, k-1):
            V[i] = S.begin()
            S.discard(S.begin())
        print(S.begin())
        for i in range(V.size()):
            S.insert(V[i])

        print(S)