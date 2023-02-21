#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        dummy = ListNode()
        dummy.next = list1

        i = 0
        p = dummy
        while i < a:
            p = p.next
            i += 1
        # 此时p.next是删除部分的第一个节点

        q = p
        while i <= b:
            q = q.next
            i += 1
        q = q.next
        # 此时q是删除部分最后一个节点的后一个节点

        r = list2
        while r.next is not None:
            r = r.next
        # 此时r是list2的尾节点

        # 拼接
        p.next = list2
        r.next = q

        return dummy.next