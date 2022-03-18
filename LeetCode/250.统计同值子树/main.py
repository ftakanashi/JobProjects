#!/usr/bin/env python
# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countUnivalSubtrees(self, root: Optional[TreeNode]) -> int:
        ans = 0
        if root is None:
            return ans

        def dfs(node):
            nonlocal ans
            l = dfs(node.left) if node.left else node.val    # 当子节点是None时不用考虑，为了和下面的判断自洽，这里直接将flag值赋值为当前节点值
            r = dfs(node.right) if node.right else node.val
            if l == r == node.val:
                ans += 1
                return node.val
            else:
                return

        dfs(root)

        return ans