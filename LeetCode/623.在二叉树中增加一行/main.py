#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def addOneRow(self, root: TreeNode, val: int, depth: int) -> TreeNode:
        if depth == 1:
            new_root = TreeNode(val)
            new_root.left = root
            return new_root

        def dfs(node, curr_depth):

            if curr_depth == depth - 1:
                new_left = TreeNode(val)
                new_right = TreeNode(val)
                new_left.left = node.left
                node.left = new_left
                new_right.right = node.right
                node.right = new_right
                return
            if node.left:
                dfs(node.left, curr_depth + 1)
            if node.right:
                dfs(node.right, curr_depth + 1)

        dfs(root, 1)
        return root

from typing import Optional
from collections import deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        if depth == 1:
            node = TreeNode(val, root, None)
            return node
        curr_depth = 1
        q = deque([])
        q.append(root)
        while q:
            for _ in range(len(q)):
                node = q.popleft()
                l, r = node.left, node.right
                if curr_depth == depth - 1:
                    new_left, new_right = TreeNode(val), TreeNode(val)
                    node.left = new_left
                    new_left.left = l
                    node.right = new_right
                    new_right.right = r
                if l:
                    q.append(l)
                if r:
                    q.append(r)
            curr_depth += 1

        return root