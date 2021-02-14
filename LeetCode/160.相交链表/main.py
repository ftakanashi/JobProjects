#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        i, j = headA, headB
        if i is None or j is None: return
        while i != j:
            i = i.next
            j = j.next
            if i is None and j is not None: i = headB
            if j is None and i is not None: j = headA
            if i is None and j is None: return
        return i