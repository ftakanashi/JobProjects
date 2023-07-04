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
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        INF = float("inf")
        ans = 0

        def dfs(node):
            if node is None:
                return True, INF, -INF, 0

            l_bst, l_min, l_max, l_sum = dfs(node.left)
            r_bst, r_min, r_max, r_sum = dfs(node.right)

            _min = min(l_min, node.val)
            _max = max(r_max, node.val)
            _bst = (l_bst and r_bst and node.val > l_max and node.val < r_min)
            _sum = l_sum + r_sum + node.val

            # 虽然上述四个值都要返回上层，但是只有 _bst 是True的时候才需要收割答案
            if _bst:
                nonlocal ans
                ans = max(ans, _sum)

            return _bst, _min, _max, _sum

        dfs(root)
        return ans