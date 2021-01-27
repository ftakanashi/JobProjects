#!/usr/bin/env python
# Definition for a binary tree node.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        def dfs(node: TreeNode):
            if node is None:
                return None, None
            left_head, left_tail = dfs(node.left)
            right_head, right_tail = dfs(node.right)

            # 发现四种情况处理都不同，只能全部写出来了。
            if left_head is None and right_head is None:
                return node, node
            elif left_head is None and right_head is not None:
                return node, right_tail
            elif left_head is not None and right_head is None:
                node.left = None
                node.right = left_head
                return node, left_tail
            else:
                node.left = None
                node.right = left_head
                left_tail.right = right_head
                return node, right_tail

        dfs(root)