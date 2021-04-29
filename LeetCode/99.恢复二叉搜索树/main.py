#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node, stack = root, []
        prev = TreeNode(float('-inf'))
        a, b = None, None
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()

            if node.val < prev.val:
                if a is not None:    # 有两组逆序的情况
                    b = node
                    break
                else:    # 仅一组逆序的情况
                    a, b = prev, node
            prev = node

            node = node.right

        a.val, b.val = b.val, a.val


class Solution2:
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        prev = TreeNode(float('-inf'))
        node = root
        a, b = None, None
        while node:
            if node.left:
                predecessor = node.left
                while predecessor.right and predecessor.right is not node:
                    predecessor = predecessor.right

                if predecessor.right is None:
                    predecessor.right = node
                    node = node.left
                else:
                    predecessor.right = None
                    if node.val < prev.val:
                        if a is not None: b = node
                        else: a, b = prev, node
                    prev = node
                    node = node.right
            else:
                if node.val < prev.val:
                    if a is not None: b = node
                    else: a, b = prev, node
                prev = node
                node = node.right

        a.val, b.val = b.val, a.val