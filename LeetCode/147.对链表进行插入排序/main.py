#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if head is None:
            return

        dummy = ListNode(None, head)
        j = head
        i = j.next

        while i is not None:
            if j.val <= i.val:
                j = i
            else:
                k = dummy
                while k.next.val <= i.val:    # 此处不用担心k越过j，因为当k.next是j的时候，已经在上面的if分支处理了
                    k = k.next
                j.next = i.next
                tmp = k.next
                k.next = i
                i.next = tmp
            i = j.next

        return dummy.next