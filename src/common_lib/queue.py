#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: queue.py
@time: 2019/4/9 23:00
@desc: 队列的实现
"""

class Queue(object):
    def __init__(self):
        self.queue=[]

    def isEmpty(self):
        return self.queue == []

    def enqueue(self,x):
        self.queue.append(x)

    def dequeue(self):
        if self.queue:
            a=self.queue[0]
            self.queue.remove(a)
            return a
        else:
            raise IndexError('queue is empty')

    def size(self):
        return len(self.queue)