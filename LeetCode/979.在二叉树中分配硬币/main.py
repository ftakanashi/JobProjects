#!/usr/bin/env python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ans = 0

        def dfs(node):
            if node is None: return 0
            nonlocal ans
            l_net = dfs(node.left)
            r_net = dfs(node.right)
            ans += abs(l_net) + abs(r_net)
            return node.val + l_net + r_net - 1

        dfs(root)
        return ans