#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: handwritten_push_back.py
@time: 2019/4/9 22:17
@desc: 第32讲：连续放入
       未知序列长度，持续放入容器，假设有n个
       采用单链表数据结构，持续放入n个节点
       不如向量持续放入n次快
"""
import time

from common_lib.link_list import Node

if __name__ == '__main__':
    n = 1000000
    header = Node()
    p = header
    start = time.process_time()
    for i in range(n):
        # 申请
        next = Node(i)
        # 链接
        p.next = next
        # 后移
        p = next
    # 终止
    p.next = None
    end = time.process_time()
    print("运行时间(s):", end-start)
    # 释放
    p = header
    while p:
        next = p.next
        del p
        p = next