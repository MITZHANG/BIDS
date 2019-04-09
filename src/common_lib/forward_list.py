#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: forward_list.py
@time: 2019/4/8 22:03
@desc: forward_list实现
"""


class forward_list(list):

    def __init__(self, length=None, initNum=None):
        self.index = 0
        if isinstance(length, int):
            super().__init__([initNum for i in range(length)])
        elif isinstance(length, list):
            super().__init__(length)
        elif not length:
            super().__init__()

    def begin(self):
        if self[0]:
            return self[0]
        else:
            return None

    def __iter__(self):
        return super().__iter__()

    def __next__(self):
        self.index += 1
        if(self.index >= len(self)):
            raise StopIteration
        return self[self.index]

    def __add__(self, other):
        if(isinstance(other, int)):
            self.index += other
            return self[self.index]

    def __str__(self):
        temp_list = self.copy()
        while None in temp_list:
            temp_list.remove(None)
        return super.__str__(temp_list)

