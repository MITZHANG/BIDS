#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: int_push_back.py
@time: 2019/4/9 22:34
@desc: 第32讲：连续放入
       采用向量数据结构，持续放入n个整数
"""
import time

from common_lib.vector import Vector

if __name__ == '__main__':
    n = 1000000
    start = time.process_time()
    V = Vector()
    for i in range(n):
        V.push_back(0)
    end = time.process_time()
    print("运行时间(s):", end - start)