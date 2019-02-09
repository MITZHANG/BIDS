#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: hello_name.py
@time: 2019/2/9 13:28
@desc: string简单使用
"""

if __name__ == '__main__':
    name = input("name = ")
    print("hello,", name)
    print(len(name))
    name = name + name
    print(name)