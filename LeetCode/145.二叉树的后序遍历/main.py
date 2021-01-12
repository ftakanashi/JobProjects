#!/usr/bin/env python
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:

        if root is None: return []

        res = []
        stack = [root, ]
        prev = root
        while len(stack) > 0:
            node = stack.pop()
            if prev is node.right:
                res.append(node.val)
                prev = node
            elif node.left is None or prev is node.left:
                if node.right is None:
                    res.append(node.val)
                    prev = node
                else:
                    stack.append(node)
                    stack.append(node.right)
            else:
                while node is not None:
                    stack.append(node)
                    node = node.left

        return res