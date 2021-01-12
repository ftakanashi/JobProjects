#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        if root.left is None and root.right is None: return True
        if root.left is None or root.right is None: return False

        def symmetric(node1: TreeNode, node2: TreeNode) -> bool:
            if node1 is None and node2 is None:
                return True
            if node1 is None or node2 is None:    # 如果一边是None一边不是，那肯定不对称了。
                return False

            # 三个条件，全满足才是对称的
            return node1.val == node2.val and symmetric(node1.left, node2.right) and symmetric(node1.right, node2.left)

        return symmetric(root.left, root.right)