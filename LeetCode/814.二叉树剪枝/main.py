#!/usr/bin/env python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(node):
            if node is None: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            if l == 0:
                node.left = None
            if r == 0:
                node.right = None
            if l == 0 and r == 0:
                return node.val
            else:
                return 1

        dfs(root)
        if root.val == 0 and root.left is None and root.right is None:
            return None
        return root