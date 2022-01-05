#!/usr/bin/env python
from typing import List

# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:    # 还可以优化
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        res = []

        def dfs(node, ans):
            if node is None: return
            if node.left is None and node.right is None:
                ans.append(node.val)
                node.val = None

            dfs(node.left, ans)
            dfs(node.right, ans)
            if node.left is not None and node.left.val is None:
                node.left = None
            if node.right is not None and node.right.val is None:
                node.right = None

        while root.val is not None:
            ans = []
            dfs(root, ans)
            res.append(ans)
        return res