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


