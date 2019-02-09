#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: common_running_times.py
@time: 2019/2/9 23:30
@desc: 第20讲：常见运行时间-给出代码并分析常见运行时间
"""

from common_lib.vector import Vector
import time
import bisect

if __name__ == '__main__':
    N = 10000000

    v = Vector(N)

    # 线性时间
    start = time.process_time()
    length = v.size()
    for i, item in enumerate(v):
        v[i] = length - i
    end = time.process_time()
    print("运行时间(s):", end-start)

    # 线对时间
    start = time.process_time()
    v.sort()
    end = time.process_time()
    print("运行时间(s):", end - start)

    # 对数时间
    start = time.process_time()
    bisect.bisect(v, 1)
    end = time.process_time()
    print("运行时间(s):", end - start)

    # 平方时间，无法使用N这个规模量
    M = 10000
    start = time.process_time()
    for i in range(M):
        for j in range(M):
            v[i] *= j
    end = time.process_time()
    print("运行时间(s):", end - start)
    # 如果是N这个规模量，需要多少时间？
    print("估计运行时间(s):", (end - start) * (N / M) * (N / M))
