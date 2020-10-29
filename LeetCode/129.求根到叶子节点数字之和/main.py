#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def sumNumbers(self, root: TreeNode) -> int:
        return self.dfs(root, 0)

    def dfs(self, root: TreeNode, parent_total: int) -> int:

        if root is None:    # 处理输入是空树，或者遍历时某个节点只有一个子节点，另一个子节点是空的情况
            return 0

        total = parent_total * 10 + root.val    # 算出当前节点的基准值
        if root.left is None and root.right is None:
            # 身处叶子节点，直接返回基准值的值
            return total
        else:
            # 非叶子节点，继续递归
            return self.dfs(root.left, total) + self.dfs(root.right, total)