#!/usr/bin/env python

from functools import lru_cache as cache

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        @cache
        def dfs(s, e):
            if s > e: return [None, ]
            if s == e: return [TreeNode(s), ]
            res = []
            for i in range(s, e+1):
                for l in dfs(s, i-1):
                    for r in dfs(i+1, e):
                        root = TreeNode(i)
                        root.left = l
                        root.right = r
                        res.append(root)

            return res

        return dfs(1, n)