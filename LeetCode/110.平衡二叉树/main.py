#!/usr/bin/env python
from typing import Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:

        def dfs(node: TreeNode) -> Tuple[bool, int]:
            if node is None:
                return True, 0
            l_flag, l_depth = dfs(node.left)
            r_flag, r_depth = dfs(node.right)
            depth = max(l_depth, r_depth) + 1
            if l_flag and r_flag and abs(l_depth - r_depth) <= 1:
                return True, depth
            else:
                return False, depth

        flag, _ = dfs(root)
        return flag