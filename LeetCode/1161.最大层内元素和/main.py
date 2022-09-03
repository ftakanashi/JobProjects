#!/usr/bin/env python
from typing import Optional

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        q = deque()
        q.append(root)
        max_sum = float('-inf')
        ans, layer = -1, 0
        while q:
            layer += 1
            curr_sum = sum(node.val for node in q)
            if max_sum < curr_sum:
                ans = layer
                max_sum = curr_sum

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return ans