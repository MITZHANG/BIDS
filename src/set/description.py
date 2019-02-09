#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: description.py
@time: 2019/2/9 20:57
@desc: 第15讲：以集合描述算法-学会用集合的语言实现算法
"""

from common_lib.set import Set
from common_lib.vector import Vector

if __name__ == '__main__':
    # 差集
    A = Set([3, 2, 1, 4, 7 ,9, 11])
    B = Set([6 ,2, 9])
    C = Vector()
    for i, a in enumerate(A):
        if a not in B:
            C.push_back(a)
    print(C)

    # 转存
    D = Set([3, 5, 1, 7, 2, 8, 0])
    E = Set()
    while not D.empty():
        if D.begin() % 2 == 0:
            E.insert(D.begin())
        D.erase(D.begin())

    print(E)

    # 动态变化
    F = Set(["English", "Ability", "Algorithm", "Faith"])
    while F.size() > 1:
        first = F.begin()
        F.erase(F.begin())
        second = F.begin()
        F.erase(F.begin())
        F.insert(first + second)

    print(F)