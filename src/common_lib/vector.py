#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: vector.py
@time: 2019/2/9 13:51
@desc: vector向量实现
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
        temp_list = self.copy()
        while None in temp_list:
            temp_list.remove(None)
        return len(temp_list)

    def front(self):
        return self[0]

    def back(self):
        return self[-1]

    def push_back(self, num):
        if len(self) == 0:
            self.append(num)
        elif self[-1] is not None:
            self.append(num)
        elif self[-1] is None:
            for i, value in enumerate(self):
                if value is None:
                    self[i] = num
                    break

    def pop_back(self):
        if self[-1] is not None:
            self.pop()
        else:
            for i, value in enumerate(self):
                if value is None:
                    self[i-1] = None
                    break

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

    # 扩展向量的长度
    def resize(self, length, initNum=None):
        if isinstance(length, int):
            self.__init__(self + [initNum for i in range(length-self.size())])

    # 判断向量是否为空
    def empty(self):
        if len(self) != 0:
            return False
        return True

    def __str__(self):
        temp_list = self.copy()
        while None in temp_list:
            temp_list.remove(None)
        return super.__str__(temp_list)

    def capacity(self):
        return len(self)


# 范围类
class Range(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second
