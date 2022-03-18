#!/usr/bin/env python
from typing import Optional, List

from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []
        queue = deque()
        queue.append(root)
        while queue:
            s = 0
            q_len = len(queue)
            for _ in range(q_len):
                node = queue.popleft()
                s += node.val
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
            ans.append(s / q_len)
        return ans