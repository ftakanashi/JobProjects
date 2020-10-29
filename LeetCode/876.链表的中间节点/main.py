#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        slow = fast = head

        while fast is not None and fast.next is not None:
            # 因为循环体里用到了fast.next.next，所以确认fast.next is not None 是一件很自然地事情
            slow = slow.next
            fast = fast.next.next

        return slow