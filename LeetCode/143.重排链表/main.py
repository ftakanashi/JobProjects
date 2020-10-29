#!/usr/bin/env python
# -*- coding:utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:

    def reverseList(self, head: ListNode) -> ListNode:
        '''
        反转链表
        '''
        prev = None
        curr = head
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev

    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if head is None:
            return

        # 查找中间节点（如果是偶数个节点则返回前半末尾，如1234返回2而不是3)
        slow = fast = head
        while fast.next and fast.next.next:    # 返回2而不是3在这里控制
            slow = slow.next
            fast = fast.next.next
        mid_node = slow

        # 将后半链表反转
        rear_node_start = mid_node.next
        mid_node.next = None    # 注意在这里切断前后两个列表，要不然就奇怪了
        mid_node = self.reverseList(rear_node_start)

        # merge
        f = head
        r = mid_node
        while f and r:
            next_f = f.next
            next_r = r.next
            f.next = r
            r.next = next_f
            f = next_f
            r = next_r