#!/usr/bin/env python

from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        in_order_map = {v: i for i, v in enumerate(inorder)}

        def build(in_s, in_e, post_e):
            if in_s > in_e: return
            if in_s == in_e: return TreeNode(inorder[in_s])
            root_v = postorder[post_e]
            pivot = in_order_map[root_v]    # 根节点在inorder中的位置
            r = in_e - pivot

            root = TreeNode(root_v)
            root.left = build(in_s, pivot - 1, post_e - r - 1)
            root.right = build(pivot + 1, in_e, post_e - 1)
            return root

        n = len(inorder)
        return build(0, n-1, n-1)