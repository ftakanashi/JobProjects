#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        def dfs(node, curr_depth):

            if curr_depth == depth - 1:
                new_left = TreeNode(val)
                new_right = TreeNode(val)
                new_left.left = node.left
                node.left = new_left
                new_right.right = node.right
                node.right = new_right
                return
            if node.left:
                dfs(node.left, curr_depth + 1)
            if node.right:
                dfs(node.right, curr_depth + 1)

        dfs(root, 1)
        return root