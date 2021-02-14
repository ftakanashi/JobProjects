#!/usr/bin/env python

# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None: return
        stack = []
        head = Node(-1)
        prev = head
        while stack or root is not None:
            while root is not None:
                stack.append(root)
                root = root.left
            node = stack.pop()

            prev.right = node
            node.left = prev
            prev = node

            root = node.right

        tail = head.right
        while tail.right is not None:
            tail = tail.right
        head.right.left = tail
        tail.right = head.right
        return head.right