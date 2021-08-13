#!/usr/bin/env python
from typing import List
from collections import defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def verticalTraversal(self, root: TreeNode) -> List[List[int]]:
        info = defaultdict(list)

        def dfs(node, x, y):
            if node is None: return
            info[y].append((node.val, x, y))
            dfs(node.left, x + 1, y - 1)
            dfs(node.right, x + 1, y + 1)

        dfs(root, 0, 0)
        res = []
        for k in sorted(info):
            nodes = info[k]
            res.append([t[0] for t in sorted(nodes, key=lambda x:(x[1], x[0]))])
        return res