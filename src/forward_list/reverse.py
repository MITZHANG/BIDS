#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: reverse.py
@time: 2019/4/9 21:45
@desc: 第31讲：逆置单链-就地逆置链表
"""
from common_lib.link_list import Node
from common_lib.vector import Vector


def traverse(header):
    p = header.next
    result = []
    while p:
        result.append(str(p.data))
        p = p.next
    print(result)

def reverse(header):
    prev = None
    curr = header.next
    while curr:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
    header.next = prev

if __name__ == '__main__':
    V = Vector([Node(), Node(1), Node(2), Node(3)])
    i = 0
    while i + 1 < len(V):
        V[i].next = V[i+1]
        i += 1
    traverse(V[0])
    reverse(V[0])
    traverse(V[0])

    FL = [1, 2, 3]
    FL.reverse()
    print(FL)