#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: just_sort.py
@time: 2019/2/9 15:45
@desc: 第5讲：数组和向量的排序
"""

from common_lib.vector import Vector

if __name__ == '__main__':
    N = 5
    a = [2, 5, 3, 1, 4]

    # 从小到大排序
    a.sort()
    print(a)

    # 从大到小排序
    a.sort(reverse=True)
    print(a)

    # 对字符串排序
    b = ["www", "algorithm", "racer", "text", "wait"]
    b.sort()
    print(b)
    b.sort(reverse=True)
    print(b)

    # 对向量排序
    v = Vector(["www", "algorithm", "racer", "text", "wait"])
    # 从小到大排序
    v.sort()
    print(v)
    # 从大到小排序
    v.sort(reverse=True)
    print(v)
    # 基于范围循环打印v中的元素
    for x in v:
        print(x, end=" ")

