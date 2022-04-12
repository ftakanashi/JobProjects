#!/usr/bin/env python
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:

        def dfs(node):
            if node is None: return
            left = dfs(node.left)
            right = dfs(node.right)
            res = f"{node.val}"
            if right is not None:
                res += f"({left if left is not None else ''})"
                res += f"({right})"
            elif left is not None:
                res += f"({left})"
            return res

        return dfs(root)