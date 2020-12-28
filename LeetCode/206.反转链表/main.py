#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return None

        prev = head
        curr = head.next
        head.next = None    # 最开始的第一个.next要切断，否则最终出现的链表最后两个节点循环引用

        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        if head.next.next is None:
            res = head.next
            res.next = head
            head.next = None
            return res
        res = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return res