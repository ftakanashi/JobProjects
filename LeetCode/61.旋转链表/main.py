#!/usr/bin/env python
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None: return

        # 第一遍扫描
        i = head
        count = 1
        while i.next is not None:
            i = i.next
            count += 1

        k = k % count
        if k == 0: return head

        # 第二遍扫描
        j = head
        for _ in range(k):
            j = j.next

        i = head
        while j.next is not None:
            i = i.next
            j = j.next

        res = i.next
        i.next = None
        j.next = head
        return res

class Solution2:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head or not head.next: return head
        i, n = head, 1
        while i.next is not None:
            n += 1
            i = i.next
        k = k % n
        i.next = head

        while n > k:
            n -= 1
            i = i.next
        res = i.next
        i.next = None
        return res