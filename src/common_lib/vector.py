#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: vector.py
@time: 2019/2/9 13:51
@desc: vector实现
"""


class Vector(list):

    def __init__(self, length=None, initNum=None):
        if isinstance(length, int):
            super().__init__([initNum for i in range(length)])
        elif isinstance(length, list):
            super().__init__(length)
        elif not length:
            super().__init__()

    def size(self):
        return len(self)

    def front(self):
        return self[0]

    def back(self):
        return self[-1]

    def push_back(self, num):
        self.append(num)

    def pop_back(self):
        self.pop()

    # 得到key的下界位置
    def lower_bound(self, key):
        low, high = 0, len(self) - 1
        pos = len(self)
        while low < high:
            mid = int((low + high) / 2)
            if self[mid] < key:
                low = mid + 1
            else:  # >=
                high = mid
                pos = high
        return pos

    # 得到key的上界位置
    def upper_bound(self, key):
        low, high = 0, len(self) - 1
        pos = len(self)
        while low < high:
            mid = int((low + high) / 2)
            if self[mid] <= key:
                low = mid + 1
            else:  # >
                high = mid
                pos = high
        return pos

    # 得到重复key的所在区间
    def equal_range(self, key):
        result = Range(self.lower_bound(key), self.upper_bound(key))
        return result

    # 删除范围内的元素
    def erase(self, first, second):
        result = self[: first] + self[second:]
        self = self.__init__(result)


# 范围类
class Range(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
