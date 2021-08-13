#!/usr/bin/env python
# Definition for a binary tree node.
from functools import lru_cache as cache

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: TreeNode) -> int:

        @cache
        def dfs(node, do):
            if node is None: return 0
            if do:
                v = node.val
                v += dfs(node.left, False)
                v += dfs(node.right, False)
            else:
                v = 0
                v += max(dfs(node.left, True), dfs(node.left, False))
                v += max(dfs(node.right, True), dfs(node.right, False))

            return v

        return max(dfs(root, True), dfs(root, False))