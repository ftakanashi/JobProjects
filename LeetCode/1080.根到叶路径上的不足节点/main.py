#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sufficientSubset(self, root: Optional[TreeNode], limit: int) -> Optional[TreeNode]:

        def dfs(node, path):
            if node is None:
                return False
            if node.left is None and node.right is None:
                return node.val + path >= limit

            l_flag = dfs(node.left, path + node.val)
            r_flag = dfs(node.right, path + node.val)
            if not l_flag:
                node.left = None
            if not r_flag:
                node.right = None
            return l_flag or r_flag

        root_flag = dfs(root, 0)
        return root if root_flag else None