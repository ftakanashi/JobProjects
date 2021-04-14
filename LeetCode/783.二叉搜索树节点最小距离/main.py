#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def minDiffInBST(self, root: TreeNode) -> int:
        prev = -float('inf')
        ans = float('inf')
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            ans = min(ans, node.val - prev)
            prev = node.val
            node = node.right

        return ans

class Solution2:
    def getMinimumDifference(self, root: TreeNode) -> int:
        ans = float('inf')
        prev = -float('inf')

        def dfs(node):
            if not node: return
            nonlocal prev
            nonlocal ans
            dfs(node.left)
            ans = min(ans, node.val - prev)
            prev = node.val
            dfs(node.right)

        dfs(root)
        return ans