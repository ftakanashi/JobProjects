#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
from typing import List
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


import collections

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        queue = collections.deque([])
        queue_bak = collections.deque([])
        queue.append(root)
        res = []
        while True:
            row = []
            while len(queue) > 0:
                node = queue.popleft()
                row.append(node.val)
                if node.left:
                    queue_bak.append(node.left)
                if node.right:
                    queue_bak.append(node.right)
            res.append(row)
            if len(queue_bak) == 0:
                break
            queue = queue_bak
            queue_bak = collections.deque([])
        return res