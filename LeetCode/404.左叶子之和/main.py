#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        def dfs(node, ident):
            if node is None: return 0
            if node.left is None and node.right is None:
                return 0 if ident != "L" else node.val

            return dfs(node.left, "L") + dfs(node.right, "R")

        return dfs(root, "R")