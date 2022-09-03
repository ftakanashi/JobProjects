#!/usr/bin/env python
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:

        to_delete = set(to_delete)
        ans = set()

        def dfs(node):
            if node is None: return

            if node.val in to_delete:
                if node in ans: ans.remove(node)
                if node.left: ans.add(node.left)
                if node.right: ans.add(node.right)

            if node.left:
                tmp = node.left
                if node.left.val in to_delete:
                    node.left = None
                dfs(tmp)

            if node.right:
                tmp = node.right
                if node.right.val in to_delete:
                    node.right = None
                dfs(tmp)

        ans.add(root)
        dfs(root)

        return list(ans)