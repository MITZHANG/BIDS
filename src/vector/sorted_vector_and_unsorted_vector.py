#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: sorted_vector_and_unsorted_vector.py
@time: 2019/2/9 20:22
@desc: 第14讲：有序向量与无序向量-基于向量的功能实现多重集合
"""

from common_lib.vector import Vector

if __name__ == '__main__':
    # 有序向量
    sv = Vector([1, 3, 6, 6, 8 ,9])
    # 插入新元素
    key = 0
    iter_sv = sv.lower_bound(key)
    sv.insert(iter_sv, key)
    # 删除元素（重复元素的最后一个）
    key = 6
    sv.remove(key)

    # 查找重复key所在的区间range, 区间为[range.first, range.second)
    key_range = sv.equal_range(key)
    # 删除整个range区间的元素
    sv.erase(key_range.first, key_range.second)
    # 打印
    print(sv)

    # 无序向量
    usv = Vector([9, 6, 1, 3, 8, 6])
    # 插入新元素
    key = 0
    usv.push_back(key)
    # 删除元素（重复元素的额第一个）
    key = 6
    usv.remove(key)
    # 打印
    print(usv)

