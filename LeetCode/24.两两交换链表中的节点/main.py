#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is None: return
        if head.next is None: return head
        dummy = ListNode(0)
        dummy.next = head
        i, j, k = dummy, head, head.next
        while k is not None:
            j.next = k.next
            k.next = j
            i.next = k
            i = j
            j = i.next if i is not None else None
            k = j.next if j is not None else None

        return dummy.next

class Solution2:
    def swapPairs(self, head: ListNode) -> ListNode:

        def rec(node: ListNode) -> ListNode:
            if node is None:
                return
            if node.next is None:
                return node
            i, j = node, node.next
            tmp = j.next
            j.next = i
            i.next = rec(tmp)
            return j

        return rec(head)