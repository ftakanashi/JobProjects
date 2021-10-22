#!/usr/bin/env python
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        prev = root
        while prev:    # prev是扫描上层节点的指针
            dummy = Node(-1)
            cur = dummy   # cur是扫描本层节点的指针
            while prev:   # 遍历扫描上层节点，并按顺序依次串联本层节点
                if prev.left:
                    cur.next = prev.left
                    cur = cur.next
                if prev.right:
                    cur.next = prev.right
                    cur = cur.next
                prev = prev.next
            prev = dummy.next    # 重置上层节点到本层节点的最左节点，为下一轮循环做准备
        return root