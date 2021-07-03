#!/usr/bin/env python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None: return head
        i, j = head, head.next
        while j is not None:
            i.next = j.next
            j.next = head
            head = j

            j = i.next

        return head

class Solution2:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        new_head = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return new_head