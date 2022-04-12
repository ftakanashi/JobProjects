#!/usr/bin/env python
from typing import List

from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestKValues(self, root: TreeNode, target: float, k: int) -> List[int]:
        ans = deque()

        def dfs(node):
            if node is None: return
            dfs(node.left)
            if len(ans) < k:
                ans.append(node.val)
            elif abs(ans[0] - target) > abs(node.val - target):
                ans.popleft()
                ans.append(node.val)
            else:
                return
            dfs(node.right)

        dfs(root)
        return list(ans)