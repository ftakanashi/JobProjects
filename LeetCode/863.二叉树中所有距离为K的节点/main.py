#!/usr/bin/env python
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        parents = {}
        start = None
        def dfs_for_parents(node):
            nonlocal start
            if node == target:    # 顺便记录起始点位置
                start = node
            if node.left:
                parents[node.left.val] = node
                dfs_for_parents(node.left)
            if node.right:
                parents[node.right.val] = node
                dfs_for_parents(node.right)

        dfs_for_parents(root)    # 第一次DFS搜索，填充父节点哈希表

        res = []
        def dfs(node, prev, dist):
            if dist == 0:
                res.append(node.val)
                return
            if node.left and prev is not node.left:    # 为了避免循环搜索，将来源除外，即来源是左子/右子/父节点时，本次不搜该方向
                dfs(node.left, node, dist - 1)
            if node.right and prev is not node.right:
                dfs(node.right, node, dist - 1)
            if node.val in parents and prev is not parents[node.val]:
                dfs(parents[node.val], node, dist - 1)

        dfs(start, None, k)    # 第二次DFS搜索

        return res