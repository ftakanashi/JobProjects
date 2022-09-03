#!/usr/bin/env python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        def dfs(node):
            if node is None: return 0, 0
            if node.left is None and node.right is None: return 0, 0

            l1, l2 = dfs(node.left)
            r1, r2 = dfs(node.right)

            a1, a2 = 0, 0
            if node.left and node.val == node.left.val:
                a1 = max(a1, l1 + 1)
            if node.right and node.val == node.right.val:
                a1 = max(a1, r1 + 1)
            if node.left and node.right and node.val == node.left.val == node.right.val:
                a2 = max(a2, l1 + r1 + 2)

            return a1, max(l1, r1, l2, r2, a2)

        res = dfs(root)
        return max(res)
