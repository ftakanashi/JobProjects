#!/usr/bin/env python
from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = head
        prev, curr = ListNode(float("-inf")), head
        while curr is not None:
            if curr.val < prev.val:
                prev.next = curr.next
                curr.next = res
                res = curr
                curr = prev.next
            else:
                prev = curr
                curr = curr.next
        return res