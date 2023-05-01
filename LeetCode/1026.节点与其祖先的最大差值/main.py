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
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if node is None:
                return float("inf"), float("-inf"), 0

            l1, l2, l3 = dfs(node.left)
            r1, r2, r3 = dfs(node.right)

            _min = min(l1, r1, node.val)
            _max = max(l2, r2, node.val)

            ans_cands = [l3, r3]
            if l1 < float("inf"):
                ans_cands.append(abs(node.val - l1))
            if r1 < float("inf"):
                ans_cands.append(abs(node.val - r1))
            if l2 > float("-inf"):
                ans_cands.append(abs(node.val - l2))
            if r2 > float("-inf"):
                ans_cands.append(abs(node.val - r2))
            _ans = max(ans_cands)
            return _min, _max, _ans

        return dfs(root)[2]