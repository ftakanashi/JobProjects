#!/usr/bin/env python

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:

        def dfs(node, num):
            num = (num << 1) + node.val
            if node.left is None and node.right is None:
                return num
            ans = 0
            if node.left:
                ans += dfs(node.left, num)
            if node.right:
                ans += dfs(node.right, num)
            return ans

        return dfs(root, 0)