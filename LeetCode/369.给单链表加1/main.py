#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution1:
    def reverse(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head
        res, p = None, head
        while p is not None:
            tmp = p.next
            p.next = res
            res = p
            p = tmp
        return res

    def plusOne(self, head: ListNode) -> ListNode:
        rev = self.reverse(head)
        p, remind = rev, 1
        while p is not None:
            p.val += remind
            if p.val == 10:
                p.val, remind = 0, 1
            else:
                remind = 0
                break
            p = p.next

        if remind == 1:
            res = ListNode(1)
            res.next  = self.reverse(rev)
        else:
            res = self.reverse(rev)
        return res


class Solution2:
    def plusOne(self, head: ListNode) -> ListNode:
        dummy = ListNode(0, head)
        p = rightmost = dummy    # rightmost: 最靠后的非9节点
        while p is not None:
            if p.val != 9:
                rightmost = p
            p = p.next

        rightmost.val += 1
        p = rightmost.next
        while p is not None:
            p.val = 0
            p = p.next
        return dummy if dummy.val == 1 else head