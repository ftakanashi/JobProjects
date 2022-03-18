#!/usr/bin/env python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        ans = None
        diff = float('inf')
        node = root
        while node:
            if node.val == target: return node.val
            elif target < node.val:
                if diff > node.val - target:
                    ans = node.val
                    diff = node.val - target
                node = node.left
            else:
                if diff > target - node.val:
                    ans = node.val
                    diff = target - node.val
                node = node.right
        return ans