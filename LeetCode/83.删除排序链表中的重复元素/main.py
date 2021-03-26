#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        i = head
        while i.next and i.next.val == i.val:
            i = i.next
        head.next = self.deleteDuplicates(i.next)
        return head

class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        i = head
        while i:
            j = i
            while j.next and j.next.val == j.val:
                j = j.next
            i.next = j.next
            i = i.next
        return head