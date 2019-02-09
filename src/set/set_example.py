#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: set_example.py
@time: 2019/2/9 18:18
@desc: 第12讲：初识集合-set的基本用法
"""

from common_lib.set import Set

if __name__ == '__main__':
    S = Set([3, 2, 1, 4, 5])

    # 放入集合
    S.insert(1)
    S.insert(7)

    # 查找和删除
    S.discard(0)
    S.discard(5)

    # 遍历集合
    for _, s in enumerate(sorted(S)):
        print(s, end=" ")
    print()
    for _, s in enumerate(sorted(S, reverse=True)):
        print(s, end=" ")