#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: pointer_push_back.py
@time: 2019/4/9 22:41
@desc: 第32讲：连续放入
       采用向量数据结构，持续放入n个节点
       由于python中没有指针的概念，故与结构体的push back是一样的
"""
import time

from common_lib.vector import Vector

global m

class xnode(object):
    def __init__(self, d):
        data = []
        for i in range(m):
            data.append(d)
        data.append(0)

if __name__ == '__main__':
    n = 1000000
    m = 16
    V = Vector()
    start = time.process_time()
    for i in range(n):
        p = xnode(i)
        V.push_back(p)
    end = time.process_time()
    print("运行时间(s):", end - start)
    for v in V:
        del v
