#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        left_head = ListNode(None)
        right_head = ListNode(None)
        left = left_head
        right = right_head
        i = head
        while i is not None:
            tmp = i.next
            i.next = None
            if i.val < x:
                left.next = i
                left = i
            else:
                right.next = i
                right = i
            i = tmp
        left.next = right_head.next
        return left_head.next