#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: vector.py
@time: 2019/2/9 13:51
@desc: vector实现
"""


class Vector(list):

    def __init__(self, length, initNum=0):
        if isinstance(length, int):
            super().__init__([initNum for i in range(length)])
        elif isinstance(length, list):
            super().__init__(length)

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

    def equal_range(self, key):
        result = Range(self.lower_bound(key), self.upper_bound(key))
        return result

    def erase(self, first, second):
        result = self[: first] + self[second:]
        self = self.__init__(result)

class Range(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second