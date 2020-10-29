#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:

        if head is None: return True    # 空链表处理

        # 寻找中间节点。如果是总结点个数是偶数个则找前半的最后一个节点。
        slow = fast = head
        while fast.next and fast.next.next:
            # 因此条件是这个而不是 fast and fast.next
            slow = slow.next
            fast = fast.next.next

        # 分割原链表，并且将后半部分翻转
        curr = slow.next
        slow.next = None
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # 用两个游标依次比对前后两个子链表
        i = head
        j = prev
        while j:
            if i.val == j.val:
                i = i.next
                j = j.next
            else:
                return False
        return True