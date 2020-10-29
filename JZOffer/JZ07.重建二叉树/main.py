#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for a binary tree node.

from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        self.inorder = inorder
        self.preorder = preorder
        root = self.cur(0, 0, len(preorder) - 1)
        return root

    def cur(self, pre_root_i, in_left_i, in_right_i):

        if in_left_i > in_right_i:
            # 结束递归条件：当某个树只有一个节点，那么此时有in_left_i == in_right_i == in_root_i
            # 自然in_left_i > in_root_i -1 以及 in_root_i + 1 > in_right_i
            # 此时return个None无伤大雅，把叶子节点的左右子节点设置成None了而已。
            return
        root_val = self.preorder[pre_root_i]
        root = TreeNode(root_val)
        in_root_i = self.inorder.index(root_val)    # 定位inorder中当前preorder发现的根节点位于什么位置
        # 构建子树。注意第一个参数稍微有点意思，是preorder中子树根节点的index
        root.left = self.cur(pre_root_i + 1, in_left_i, in_root_i - 1)
        root.right = self.cur(pre_root_i + in_root_i - in_left_i + 1,in_root_i + 1, in_right_i)

        return root