#!/usr/bin/env python
from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def printTree(self, root: Optional[TreeNode]) -> List[List[str]]:

        def get_depth(node):
            if node is None: return 0
            return max(get_depth(node.left), get_depth(node.right)) + 1

        depth = get_depth(root)

        ans = [["" for _ in range(2 ** depth - 1)] for _ in range(depth)]

        def dfs(node, x, y, span):
            if node is None: return
            ans[x][y - 1] = str(node.val)
            dfs(node.left, x + 1, y - span, span // 2)
            dfs(node.right, x + 1, y + span, span // 2)

        dfs(root, 0, (2 ** depth) // 2, (2 ** depth) // 2 // 2)
        return ans