#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: diagonal.py
@time: 2019/2/9 14:21
@desc: 对角线问题
"""

import numpy as np


def displayM(label,M):
    print(label)
    print(np.mat(M))


if __name__ == '__main__':

    n = 64
    x = 4
    y = 2
    M = [[0 for j in range(n)] for i in range(n)]

    # 方法1
    for i in range(n):
        for j in range(n):
            if i == j:
                M[i][j] = x
            else:
                M[i][j] = y

    displayM("方法1" ,M)

    # 方法2
    for i in range(n):
        for j in range(n):
            M[i][j] = y
    for i in range(n):
        M[i][i] = x

    displayM("方法2" ,M)

    # 方法3
    for i in range(n):
        for j in range(n):
            M[i][j] = y
        M[i][i] = x
        for j in range(i+1, n):
            M[i][j] = y
    displayM("方法3" ,M)
