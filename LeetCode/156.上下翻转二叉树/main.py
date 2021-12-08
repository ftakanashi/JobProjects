#!/usr/bin/env python
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def upsideDownBinaryTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None or root.left is None:
            return root

        def dfs(node):
            if node.left.left is None:
                L, R = node.left, node.right
                node.left = node.right = None
                L.left = R
                L.right = node
                return L, node
            new_root, new_tail = dfs(node.left)
            new_tail.left = node.right
            node.left = node.right = None
            new_tail.right = node
            return new_root, node

        ans, _ = dfs(root)
        return ans