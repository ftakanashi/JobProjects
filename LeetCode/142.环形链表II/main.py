#!/usr/bin/env python
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution1:
    def detectCycle(self, head: ListNode) -> ListNode:
        visited = set()
        node = head
        while node is not None:
            if node in visited:
                return node
            visited.add(node)
            node = node.next

class Solution2:
    def detectCycle(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return
        i = head.next
        j = head.next.next
        while j is not None and j.next is not None:
            i = i.next
            j = j.next.next
            if i == j:
                break    # 快慢指针相遇点

        if j is None or j.next is None:
            return    # 排除无环情况

        p = head    # 一个新的指针
        while p != i:
            p = p.next
            i = i.next
        return p    # 两者相遇时返回