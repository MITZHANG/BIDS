#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: phone.py
@time: 2019/4/21 17:58
@desc: 第37讲: 电话号码排序
"""
from queue import Queue

from common_lib.vector import Vector

if __name__ == '__main__':
    # 字符串长度
    L = 9
    # 基数
    B = 10
    # 如果是特别长的字符串，可以考虑用链表存储原始数据，后续队列也用链表实现
    # 不要用字符串向量再配上字符串指针向量来变动操作，那样效果不好
    phone_numbers = Vector(10, "123456789")
    Q = Vector(B)
    # d从L - 1到0，注意用法
    d = L
    while d > 0:
        d -= 1
        for x in phone_numbers:
            if not Q[ord(x[d]) - ord('0')]:
                Q[ord(x[d]) - ord('0')] = Queue()
            Q[ord(x[d]) - ord('0')].put(x)
        i = 0
        for k in range(B):
            while Q[k] and not Q[k].empty():
                phone_numbers[i] = Q[k].get()
                i += 1

