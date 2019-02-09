#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: binary_search_array.py
@time: 2019/2/9 16:01
@desc: 第7讲：数组二分查找
"""

# key: 要查找的关键字，data: 数组，N: 数组长度
def binary_search_array(key, data, N):
    if N < 0:
        return -1

    low = 0
    high = N - 1
    while low <= high:
        mid = int(low + (high - low) / 2)
        if key < data[mid]:
            high = mid - 1
        elif data[mid] < key:
            low = mid + 1
        else:
            return mid

    return -1


if __name__ == '__main__':
    a = [1, 2, 3, 4, 5]
    print(binary_search_array(2, a, 5))
    print(binary_search_array(0, a, 5))
    print(binary_search_array(2, a[2:], 3))
    print(binary_search_array(0, a, 0))

