#!/usr/bin/env python

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if root is None: return 0

        def dfs(node):
            if not node.children: return 1
            max_depth = max(
                dfs(child) for child in node.children
            )
            return max_depth + 1

        return dfs(root)