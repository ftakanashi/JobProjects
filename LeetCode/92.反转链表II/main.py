#!/usr/bin/env python

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if head is None or head.next is None or m == n: return head
        dummy = ListNode(-1)
        dummy.next = head
        i = dummy
        count = 0

        while count < m - 1:
            i = i.next
            count += 1
        prev = i
        tail = i = i.next
        prev.next = None    # 打断第m个节点前的连接

        # 开始反转
        last_node = None
        while count < n:
            tmp = i.next
            i.next = last_node
            last_node = i
            i = tmp
            count += 1    # 反转时别忘了计数

        # 到此处，反转操作已经完成并且反转后片段和前、后两片段是断开的。
        # 重新整理连接：
        prev.next = last_node
        tail.next = i
        return dummy.next