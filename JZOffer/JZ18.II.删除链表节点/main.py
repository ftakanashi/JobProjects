#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        if head is None: return    # 空链表
        if head.val == val: return head.next    # 要删除的是head

        i = head
        while i.next is not None and i.next.val != val:
            i = i.next

        if i.next is None:    # 跳出条件是i.next is None，此时扫描完了整个链表但是没有找到val值节点
            return head
        else:
            i.next = i.next.next    # 删除节点

        return head