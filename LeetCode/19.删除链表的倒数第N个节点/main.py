#!/usr/bin/env python
# Definition for singly-linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head
        i = j = dummy
        for _ in range(n):
            j = j.next

        while j.next is not None:
            i = i.next
            j = j.next

        i.next = i.next.next    # 无需检查i.next是否是None。因为只要n是有效的，那么i.next永远不是None

        return dummy.next    # 注意不是返回head，否则如果删除的是head本身的话就会报错。