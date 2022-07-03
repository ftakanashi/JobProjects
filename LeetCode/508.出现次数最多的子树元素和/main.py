#!/usr/bin/env python
from typing import List

from collections import Counter

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findFrequentTreeSum(self, root: TreeNode) -> List[int]:
        res = []

        def dfs(node: TreeNode) -> int:
            if node is None: return 0
            s = node.val + dfs(node.left) + dfs(node.right)
            res.append(s)
            return s

        dfs(root)

        counter = Counter(res)
        max_time = max(counter.values())
        ans = []
        for s in counter:
            if counter[s] == max_time:
                ans.append(s)
        return ans