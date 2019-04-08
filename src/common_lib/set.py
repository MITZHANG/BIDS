#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: set.py
@time: 2019/2/9 18:19
@desc: set集合实现
"""

class Set(set):

    def __init__(self, array=None):
        if isinstance(array, list):
            super().__init__(array)
        elif not array:
            super().__init__()

    def insert(self, num):
        self.add(num)

    def begin(self):
        return min(sorted(self.copy()))

    def end(self):
        return None

    def find(self, num):
        return

    def size(self):
        return len(self)

    def empty(self):
        if len(self) == 0:
            return True
        return False

    def erase(self, num):
        self.discard(num)

