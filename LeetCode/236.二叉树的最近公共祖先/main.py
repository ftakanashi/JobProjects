#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node: TreeNode):
            if node is None or node in (p, q): return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right: return node
            if left is None: return right
            if right is None: return left
            return

        return dfs(root)