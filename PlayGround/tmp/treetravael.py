#!/usr/bin/env python
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def midorder(root: TreeNode):
    stack = []
    res = []
    node = root
    while stack:
        while node:
            stack.append(node)
            node = node.left
        node = stack.pop()
