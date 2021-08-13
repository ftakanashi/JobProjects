#!/usr/bin/env python
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, target: int) -> List[List[int]]:
        res = []
        if root is None: return res

        def dfs(node: TreeNode, path: List[int]):
            if node.left is None and node.right is None:
                if sum(path) + node.val == target:
                    res.append(path + [node.val, ])
                    return
            if node.left is not None:
                dfs(node.left, path + [node.val, ])
            if node.right is not None:
                dfs(node.right, path + [node.val, ])

        dfs(root, [])
        return res