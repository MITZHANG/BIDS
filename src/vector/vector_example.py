#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: vector_example.py
@time: 2019/2/13 21:09
@desc: 第24讲-向量用法
"""

from common_lib.vector import Vector

if __name__ == '__main__':
    # 定义一个初始长度为10的向量A, 可用位置数为10.
    A = Vector(10)
    # 下标i从0到A.size()-1对A中每个元素赋值i.
    # 由于python的list可以放置任何类型元素
    # 向量的下标用法与数组相同, 但要注意应保证向量中实有元素个数就是size().
    for i in range(A.size()):
        A[i] = i
    for i in range(A.size()):
        A[i] = 1

    # 定义一个长度为5的向量B, 初始元素全为3.
    B = Vector(5, 3)
    # 在向量B末尾加入100个2.
    B.resize(B.size() + 100, 2)
    # 在向量V的尾部加入4
    B.push_back(4)
    # 迭代器的另一种用法，使用列表推导
    B = Vector([value*2 for i, value in enumerate(B)])
    # 若向量B不为空，则持续输出其尾部元素并删除之
    while not B.empty():
        # 输出向量V的末尾元素
        print(B.back())
        # 删除向量V的末尾元素
        B.pop_back()

    # 接收未知长度的自然数输入序列, 以负数作为输入终止
    C = Vector()
    # 基于push_back操作的速度非常快.
    while True:
        num = int(input())
        if num >= 0:
            C.push_back(num)
        else:
            break
    print(C)


