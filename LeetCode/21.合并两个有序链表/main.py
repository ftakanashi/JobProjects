#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        res = dummy
        i, j = l1, l2
        while i is not None and j is not None:
            if i.val <= j.val:
                tmp = i.next
                i.next = None
                res.next = i
                res = i
                i = tmp
            else:
                tmp = j.next
                j.next = None
                res.next = j
                res = j
                j = tmp

        if i is not None:
            res.next = i
        if j is not None:
            res.next = j
        return dummy.next