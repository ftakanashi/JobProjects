#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        count = [0,]

        def dfs(node: TreeNode):
            if node.left is None and node.right is None:
                count[0] += 1
                return node.val if count[0] == k else None

            if node.left:
                l_ans = dfs(node.left)
                if l_ans is not None: return l_ans
            count[0] += 1
            if count[0] == k: return node.val
            if node.right:
                r_ans = dfs(node.right)
                if r_ans is not None: return r_ans

        return dfs(root)