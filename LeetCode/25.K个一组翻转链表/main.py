#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverse(self, start, end):
        i, j = None, start
        while i is not end:
            tmp = j.next
            j.next = i
            i, j = j, tmp
        start.next = j    # 翻转后的尾是最开始的start，将其next接到翻转前尾的next，从而实现翻转片段与后续片段的连接
        return end, start

    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.next is None: return head
        dummy = ListNode(0, next=head)
        prev = dummy
        while True:
            i = j = prev.next
            count = 1
            while j is not None and count < k:
                j = j.next
                count += 1
            if j is None: break
            rev_head, rev_end = self.reverse(i, j)
            prev.next = rev_head    # 翻转片段与前序片段的连接
            prev = rev_end

        return dummy.next