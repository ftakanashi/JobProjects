#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:

        def dfs(node: TreeNode):
            if node is None or (node.left is None and node.right is None): return 0, 0

            left_dep, left_diam = dfs(node.left)
            right_dep, right_diam = dfs(node.right)
            dep = max(left_dep, right_dep) + 1

            diam = left_dep + right_dep
            if node.left is not None: diam += 1
            if node.right is not None: diam += 1
            diam = max(left_diam, right_diam, diam)

            return dep, diam

        return dfs(root)[1]