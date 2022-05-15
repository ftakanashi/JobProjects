#!/usr/bin/env python
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:

        def rec(start, end):
            if start > end:
                return

            max_v = float('-inf')
            max_pos = -1
            for i in range(start, end + 1):
                if nums[i] > max_v:
                    max_v = nums[i]
                    max_pos = i
            node = TreeNode(max_v)
            node.left = rec(start, max_pos - 1)
            node.right = rec(max_pos + 1, end)
            return node

        return rec(0, len(nums) - 1)