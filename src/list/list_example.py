#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: list_example.py
@time: 2019/4/8 22:14
@desc: 第27讲：初识链表-forward_list和list的使用
"""

from common_lib.forward_list import forward_list


if __name__ == '__main__':
    # 前向链表（只维护前向指针）
    A = forward_list([1, 2, 3])
    ia = A.begin()
    print(ia)
    print(A+1)
    # 双向链表，由于python中的列表就有链表的特性，故可以作为替代
    B = [1, 2, 3]
    ib = iter(B)
    print(next(ib))
    print(next(ib))





