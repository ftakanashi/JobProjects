#!/usr/bin/env python
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def boundaryOfBinaryTree(self, root: TreeNode) -> List[int]:
        if root.left is None and root.right is None:
            return [root.val, ]

        left = []
        node = root.left
        while node is not None:
            if node.left is None and node.right is None: break
            left.append(node.val)
            node = node.left if node.left else node.right

        right = []
        node = root.right
        while node is not None:
            if node.left is None and node.right is None: break
            right.append(node.val)
            node = node.right if node.right else node.left
        right.reverse()

        leaf = []
        def dfs(node):
            if node is None or (node.left is None and node.right is None):
                if node: leaf.append(node.val)
                return
            dfs(node.left)
            dfs(node.right)
        dfs(root)

        ans = [root.val] + left + leaf + right
        return ans