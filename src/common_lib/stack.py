#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: stack.py
@time: 2019/4/9 22:59
@desc: 栈的实现
"""

class Stack(object):
    def __init__(self):
        self._stack=[]

    def isEmpty(self):
        return len(self._stack) == 0

    def push(self,item):
        self._stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self._stack.pop()

    def top(self):
        if self.isEmpty():
            raise Empty('Stack is empty')
        return self._stack[-1]

    def size(self):
        return len(self._stack)


class Empty(Exception):
    pass

