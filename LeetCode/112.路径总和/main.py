#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None: return False

        def dfs(node: TreeNode, current_sum: int) -> bool:
            if node.left is None and node.right is None:
                return current_sum + node.val == sum

            if node.left is not None:
                if dfs(node.left, current_sum + node.val):
                    return True
            if node.right is not None:
                if dfs(node.right, current_sum + node.val):
                    return True

            return False

        return dfs(root, 0)