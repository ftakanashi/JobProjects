#!/usr/bin/env python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if root is None: return 0
        gain = {}
        # 第一次DFS，将所有节点和其对应的gain保存到哈希表中
        def calc_gain(node: TreeNode) -> int:
            if node is None: return 0
            gain[node] = max(
                calc_gain(node.left),
                calc_gain(node.right),
                0
            ) + node.val
            return gain[node]
        calc_gain(root)

        # 第二次DFS，遍历每个节点并且计算该节点的两类路径中最大可拿到的路径和。
        ans = float('-inf')
        def dfs(node: TreeNode) -> int:
            if node is None: return
            nonlocal ans
            one_way = gain[node]
            v_route = node.val + gain.get(node.left, 0) + gain.get(node.right, 0)
            ans = max(ans, one_way, v_route)
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return ans