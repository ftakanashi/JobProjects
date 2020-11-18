#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None or head.next.next is None: return head
        head_i = i = head
        head_j = j = head.next

        while True:
            i.next = i.next.next
            i = i.next

            j.next = j.next.next
            j = j.next

            if j is None or j.next is None:
                i.next = head_j
                break

        return head_i
