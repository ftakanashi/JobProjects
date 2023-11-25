#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ans = [0, ]

        def dfs(node, prev_max):
            if node is None: return
            if prev_max <= node.val:    # 注意相等时也要计入
                prev_max = node.val
                ans[0] += 1
            dfs(node.left, prev_max)
            dfs(node.right, prev_max)

        dfs(root, float("-inf"))
        return ans[0]