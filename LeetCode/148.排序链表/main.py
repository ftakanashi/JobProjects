#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head

        i = j = head
        while j.next is not None and j.next.next is not None:
            i = i.next
            j = j.next.next
        mid = i.next
        i.next = None

        head = self.sortList(head)
        mid = self.sortList(mid)

        i, j = head, mid
        dummy = ListNode()
        tail = dummy
        while i is not None and j is not None:
            if i.val <= j.val:
                tail.next = i
                i = i.next
            else:
                tail.next = j
                j = j.next

            tail = tail.next
            # tail.next = None

        while i is not None:
            tail.next = i
            i = i.next
            tail = tail.next
        while j is not None:
            tail.next = j
            j = j.next
            tail = tail.next

        return dummy.next