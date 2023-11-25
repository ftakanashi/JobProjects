#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1, p2 = l1, l2
        remind = 0
        ans = dummy = ListNode(-1)    # ans是一个动态指针，指向当前答案的最尾端。dummy是用来返回答案的
        while p1 is not None and p2 is not None:
            tmp = p1.val + p2.val + remind
            val, remind = tmp % 10, tmp // 10
            ans.next = ListNode(val)
            ans, p1, p2 = ans.next, p1.next, p2.next

        while p1 is not None:
            tmp = p1.val + remind
            val, remind = tmp % 10, tmp // 10
            ans.next = ListNode(val)
            ans, p1 = ans.next, p1.next
        while p2 is not None:
            tmp = p2.val + remind
            val, remind = tmp % 10, tmp // 10
            ans.next = ListNode(val)
            ans, p2 = ans.next, p2.next
        if remind > 0:
            ans.next = ListNode(1)

        return dummy.next