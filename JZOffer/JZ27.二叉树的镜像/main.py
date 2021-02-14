#!/usr/bin/env python
# Definition for a binary tree node.
import collections
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None: return
        l, r = self.mirrorTree(root.left), self.mirrorTree(root.right)
        root.left, root.right = r, l
        return root

class Solution2:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if root is None: return
        queue = collections.deque([])
        queue.append(root)
        while queue:
            node = queue.popleft()
            if node is None: continue
            l, r = node.left, node.right
            node.right, node.left = l, r
            queue.append(node.left)
            queue.append(node.right)
        return root