#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: TreeNode, subRoot: TreeNode) -> bool:

        def dfs(p1, p2):
            if not all([p1, p2]):
                return p1 is None and p2 is None
            if p1.val != p2.val: return False
            return dfs(p1.left, p2.left) and dfs(p1.right, p2.right)

        def traverse_root(node):
            if node is None:
                return False
            elif dfs(node, subRoot):
                return True
            else:
                return traverse_root(node.left) or traverse_root(node.right)

        return traverse_root(root)


