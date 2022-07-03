#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        new = TreeNode(val)
        if root is None: return new
        node = root
        while True:
            if val < node.val:
                if node.left is None: break
                node = node.left
            else:
                if node.right is None: break
                node = node.right

        if val < node.val:
            node.left = new
        else:
            node.right = new

        return root