#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: buffer.py
@time: 2019/4/20 18:05
@desc: 第35讲: 循环队列-讲清来龙去脉
       需要考虑push(x), pop(), full(), empty()
"""

from queue import Queue
from common_lib.vector import Vector

if __name__ == '__main__':
    buffer = Vector()
    # 容量取10
    C = 10
    # 真实buffer长度为N
    N = C + 1
    buffer.resize(N)
    # 初值任选buffer中的一个有效位置
    front = int(N / 2)
    # 这里都取N / 2
    rear = int(N / 2)
    x = 0
    # 当buffer不满, 持续放入0, 1, ... , C - 1
    # 代替取模运算front = (rear+1) % N
    while (rear + 1 != front if rear + 1 < N else 0 != front):
        buffer[rear] = x
        x += 1
        # 下面的操作比rear = (rear + 1) % N更快
        if rear < C:
            rear += 1
        else:
            rear = 0

    # 当buffer不空, 持续输出队首元素并出队
    while front != rear:
        if front < C:
            front += 1
        else:
            front = 0

    # 直接使用队列
    Q = Queue()
    for x in range(C):
        Q.put(x)
    while not Q.empty():
        print(Q.get(), end=" ")

