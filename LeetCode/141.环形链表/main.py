#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def hasCycle(self, head: ListNode) -> bool:
        node = head
        while node is not None:
            if node.val is None:
                return True
            node.val = None
            node = node.next
        return False

class Solution2:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None: return False
        i, j = head, head.next
        while j is not None and j.next is not None:
            if j is i or j.next is i:
                return True
            i = i.next
            j = j.next.next

        return False