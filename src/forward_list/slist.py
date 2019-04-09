#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: slist.py
@time: 2019/4/9 21:01
@desc: 第30讲：单链实例-简单的链表实例
"""
from common_lib.link_list import LinkList, Node
from common_lib.vector import Vector

if __name__ == '__main__':
    link_list = LinkList([1,2,3])
    print(link_list)

    V = Vector([Node(1), Node(2), Node(3)])
    link_list = LinkList()
    for p in V:
        link_list.append(p)
    print(link_list)

