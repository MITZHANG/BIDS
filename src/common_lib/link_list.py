#!/usr/bin/env python
# encoding: utf-8
"""
@author: HuRuiFeng
@file: link_list.py
@time: 2019/4/9 20:48
@desc: 链表的实现
"""

class Node(object):
    def __init__(self, val=None, p = 0):
        self.data = val
        self.next = p

    def __str__(self):
        return "Node[" + str(self.data) + "]"

class LinkList(object):
    def __init__(self, data = None):
        if data is None:
            data = []
        self.head = 0
        self._initlist(data)

    def __getitem__(self, key):
        if self.is_empty():
            print('linklist is empty.')
            return
        elif key < 0 or key > self.getlength():
            print('the given key is error')
            return
        else:
            return self.getitem(key)

    def __setitem__(self, key, value):
        if self.is_empty():
            print('linklist is empty.')
            return
        elif key < 0  or key > self.getlength():
            print('the given key is error')
            return
        else:
            self.delete(key)
            return self.insert(key)

    def _initlist(self,data):
        if len(data) == 0:
            self.head = 0
        else:
            self.head = Node(data[0])
        p = self.head

        for i in data[1:]:
            node = Node(i)
            p.next = node
            p = p.next

    def getlength(self):
        p =  self.head
        length = 0
        while p != 0:
            length += 1
            p = p.next
        return length

    def is_empty(self):
        if self.getlength() == 0:
            return True
        else:
            return False

    def clear(self):
        self.head = 0

    def append(self,item):
        if isinstance(item, Node):
            q = item
        else:
            q = Node(item)
        if self.head == 0:
            self.head = q
        else:
            p = self.head
            while p.next != 0:
                p = p.next
            p.next = q

    def getitem(self,index):
        if self.is_empty():
            print('Linklist is empty.')
            return
        j = 0
        p = self.head

        while p.next != 0 and j < index:
            p = p.next
            j += 1

        if j == index:
            return p.data
        else:
            print('target is not exist!')

    def insert(self,index,item):
        if self.is_empty() or index<0 or index >self.getlength():
            print('Linklist is empty.')
            return

        if index ==0:
            q = Node(item, self.head)
            self.head = q
        p = self.head
        post  = self.head
        j = 0
        while p.next!=0 and j<index:
            post = p
            p = p.next
            j+=1

        if index ==j:
            q = Node(item,p)
            post.next = q
            q.next = p

    def delete(self, index):
        if self.is_empty() or index<0 or index >self.getlength():
            print('Linklist is empty.')
            return

        if index == 0:
            q = Node(None, self.head)
            self.head = q

        p = self.head
        post  = self.head
        j = 0
        while p.next != 0 and j < index:
            post = p
            p = p.next
            j += 1

        if index == j:
            post.next = p.next

    def index(self,value):
        if self.is_empty():
            print('Linklist is empty.')
            return
        p = self.head
        i = 0
        while p.next != 0 and not p.data == value:
            p = p.next
            i += 1
        if p.data == value:
            return i
        else:
            return -1

    def __str__(self):
        p = self.head
        result = [str(p)]
        while p.next != 0:
            p = p.next
            result.append(str(p))
        return " -> ".join(result)
