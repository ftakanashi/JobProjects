#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head

        dummy = ListNode(None)
        dummy.next = head
        i = j = head
        k = dummy

        while j.next is not None:
            if j.next.val == i.val:
                while j.next is not None and j.next.val == i.val:
                    j = j.next    # 扩展区间
                # 其实这里，跳出条件不同。如果跳出条件是前者，那么显然这个区间一直绵延到了链表最末尾...1
                # 如果是后者，则正常操作即可
                k.next = j.next
                i = j = k.next
            else:
                k, i, j = k.next, i.next, j.next

            if j is None: break    # 这里回收...1

        return dummy.next

class Solution2:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None: return head    # 递归跳出条件

        if head.val == head.next.val:
            while head.next is not None and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)    # 没有接前缀而是直接return，说明这里发生了lstrip
        else:
            head.next = self.deleteDuplicates(head.next)    # 接上
            return head

