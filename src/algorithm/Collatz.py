#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: Collatz.py
@time: 2019/2/9 16:26
@desc: 第9讲：3n + 1问题
给定一个正整数，如果是奇数，得到3n+1，如果是偶数，得到n/2
"""

from common_lib.vector import Vector

# L为计算次数
def iterative_Collatz(n):
    if n < 1:
        return 0
    L = 1
    while n != 1:
        n = int(n/2 if n%2 == 0 else 3*n + 1)
        L = L + 1
    return L

# D为计算次数
def memoized_Collatz(v, n):
    D = 0
    # 如果n不在向量v的下标范围之内, 先转换到合理范围之内并计算偏移D
    while n >= len(v):
        n = int(n/2 if n%2 == 0 else 3*n + 1)
        D = D + 1

    # 对v[n]进行赋值, 注意此处n在向量v的下标范围之内, 直接递归加1赋值即可
    if v[n] == 0 and n > 0:
        v[n] = memoized_Collatz(v, int(n / 2 if n % 2 == 0 else 3 * n + 1)) + 1

    # 返回值是原有的n对应的序列长度, 应加上偏移量D
    return v[n] + D


if __name__ == '__main__':
    # 利用备忘录保存已算出的值, 适合多次求解
    m = 10000
    v = Vector(m, 0)
    v[1] = 1

    # 测试迭代和备忘录计算结果是否一致, 测试范围为[1, max]
    max = 100000
    equal = True
    for n in range(1, max+1):
        if iterative_Collatz(n) != memoized_Collatz(v, n):
            equal = False
    print("相符" if equal else "不相符")

