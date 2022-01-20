#!/usr/bin/env python

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        ans = []
        cand, count, max_count = None, 0, 0

        def dfs(node):
            if node is None: return
            nonlocal cand
            nonlocal count
            nonlocal max_count
            dfs(node.left)
            if node.val == cand:
                count += 1
            else:
                cand = node.val
                count = 1
            if count > max_count:
                ans.clear()
                ans.append(cand)
                max_count = count
            elif count == max_count:
                ans.append(cand)
            dfs(node.right)

        dfs(root)
        return ans