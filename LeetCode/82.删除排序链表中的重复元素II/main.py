#!/usr/bin/env python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head

        if head.val == head.next.val:
            while head.next is not None and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head


class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = ListNode(-1, head)
        i, j = dummy, head
        while j:
            changed = False
            while j.next and j.val == j.next.val:
                j = j.next
                changed = True
            if changed:
                i.next = j.next
                j = j.next
            else:
                i, j = i.next, j.next
        return dummy.next