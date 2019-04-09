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
        self.stack=[]

    def isEmpty(self):
        return self.stack == []

    def push(self,item):
        self.stack.append(item)

    def pop(self):
        if self.isEmpty():
            raise IndexError('pop from empty stack')
        return self.stack.pop()

    def peek(self):
        return self.stack[-1]

    def size(self):
        return len(self.stack)