#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:

        if len(preorder) == 0: return

        index_map = {}
        for i, n in enumerate(inorder):
            index_map[n] = i

        def build(pre_i: int, l: int, r: int) -> TreeNode:
            if l > r: return

            root_v = preorder[pre_i]
            root = TreeNode(root_v)

            if l == r: return root

            pivot = index_map[root_v]
            root.left = build(pre_i + 1, l, pivot - 1)
            root.right = build(pre_i + (pivot - l) + 1, pivot + 1, r)
            return root

        return build(0, 0, len(inorder) - 1)