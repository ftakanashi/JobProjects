#!/usr/bin/env python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        s = 0
        def dfs(node):
            nonlocal s
            if node is None: return
            dfs(node.right)
            s += node.val
            node.val = s
            dfs(node.left)
        dfs(root)
        return root