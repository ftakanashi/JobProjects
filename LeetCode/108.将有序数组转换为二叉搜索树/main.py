#!/usr/bin/env python
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:

        def rec(left: int, right: int):
            if left > right:
                return
            if left == right:
                return TreeNode(nums[left])

            mid = (left + right) // 2
            node = TreeNode(nums[mid])
            node.left = rec(left, mid - 1)
            node.right = rec(mid + 1, right)
            return node

        return rec(0, len(nums) - 1)