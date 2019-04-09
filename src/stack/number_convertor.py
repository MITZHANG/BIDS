#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: number_convertor.py
@time: 2019/4/9 23:14
@desc: 第34讲：进制转换-利用栈和映射转换进制
       以b为基的表达形式(2<=b<=16)
       字符串 0, 1,..., 9, A, B,..., F
       转换为 0, 1,..., 9, 10, 11,..., 15
"""

import math
from common_lib.stack import Stack

def convertor_with_stack(number , b):
    d2c = "0123456789ABCDEF"
    # 实际上是栈，但这里用字符串更方便
    result = ""
    if number < 0:
        result += "-"
        number = -number
    S = Stack()
    while True:
        S.push(d2c[number%b])
        number = int(math.modf(number/b)[1])
        if number == 0:
            break
    while not S.isEmpty():
        result += S.top()
        S.pop()
    print(result)

def convertor_with_string(number, b):
    d2c = "0123456789ABCDEF"
    # 实际上是栈，但这里用字符串更方便
    result = ""
    if number < 0:
        result += "-"
        number = -number
        start = 1
    while True:
        result += d2c[number%b]
        number = int(math.modf(number / b)[1])
        if number == 0:
            break
    # 由于使用了字符串, 我们直接逆置字符串
    # 当然也可前面先单独保留'-'字符等逆置结束后再拼接
    print(result[::-1])

if __name__ == '__main__':
    number = int(input("请输入需要转换的数:"))
    b = int(input("请输入所转换的进制(2-16之间):"))
    if 2 <= b <= 16:
        convertor_with_stack(number, b)
        convertor_with_string(number, b)
    else:
        print("进制输入有误!")
