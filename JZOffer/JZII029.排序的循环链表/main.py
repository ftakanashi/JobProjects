#!/usr/bin/env python

# Definition for a Node.
class Node:
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class Solution:
    def insert(self, head: 'Node', insertVal: int) -> 'Node':
        new_node = Node(insertVal)
        # 两种特殊情况的处理
        if head is None:
            new_node.next = new_node
            return new_node
        if head.next is None:
            head.next = new_node
            return head

        # 开始双指针遍历
        cur, nxt = head, head.next
        while nxt is not head:
            if cur.val <= insertVal <= nxt.val:
                break
            if cur.val > nxt.val and (insertVal < nxt.val or insertVal > cur.val):
                break
            cur = cur.next
            nxt = nxt.next
        # 运行到这个点时总共有三种情况，
        # 第一、二分别对应上面的两个break
        # 第三种情况是遍历完整个链条而没有break，比如一个全部节点同值的链表
        cur.next = new_node
        new_node.next = nxt

        return head