#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: TreeNode, targetSum: int) -> int:
        if root is None: return 0

        def dfs(node, s):
            if node is None:
                return 0

            res = 0
            if node.val + s == targetSum:
                res += 1

            res += dfs(node.left, s + node.val)
            res += dfs(node.right, s + node.val)
            return res

        ans = dfs(root, 0)
        ans += self.pathSum(root.left, targetSum)
        ans += self.pathSum(root.right, targetSum)
        return ans