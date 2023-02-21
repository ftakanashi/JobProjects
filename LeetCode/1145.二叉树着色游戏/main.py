#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def btreeGameWinningMove(self, root: Optional[TreeNode], n: int, x: int) -> bool:
        count_map = {}    # 节点值 -> 该节点子树的总结点数
        node_map = {}    # 节点值 -> 节点对象

        # 获取子树总结点数的dfs函数
        def dfs(node):
            if node is None: return 0
            cnt = dfs(node.left) + dfs(node.right) + 1
            count_map[node.val] = cnt
            node_map[node.val] = node
            return cnt

        dfs(root)

        total = count_map[root.val]

        # 第一种获胜的情况
        if total - count_map[x] > count_map[x]:
            return True

        # 第二种获胜的情况
        l, r = node_map[x].left, node_map[x].right
        if total - count_map[l.val] < count_map[l.val] or total - count_map[r.val] < count_map[r.val]:
            return True

        return False