#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: binary_search_vector.py
@time: 2019/2/9 16:14
@desc:第8讲：向量二分查找
"""

from common_lib.vector import Vector


def binary_search_vector(key, data, N):
    low = 0
    high = N
    while low < high:
        mid = int(low + (high - low) / 2)
        if key < data[mid]:
            high = mid
        elif data[mid] < key:
            low = mid + 1
        else:
            return True
    return False


if __name__ == '__main__':
    v = Vector([1, 2, 3, 4, 5])
    print(binary_search_vector(2, v, 5))
    print(binary_search_vector(0, v, 5))
    print(binary_search_vector(2, v[2:], 3))
    print(binary_search_vector(0, v, 0))