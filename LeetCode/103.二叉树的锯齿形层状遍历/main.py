#!/usr/bin/env python

from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import collections

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if root is None: return []
        queue = collections.deque([])
        queue_bak = collections.deque([])
        queue.append(root)
        res = []
        rev_flag = False
        while True:
            row = []
            while len(queue) > 0:
                node = queue.popleft()

                if rev_flag:
                    row.insert(0, node.val)
                else:
                    row.append(node.val)

                if node.left is not None:
                    queue_bak.append(node.left)
                if node.right is not None:
                    queue_bak.append(node.right)

            res.append(row)
            if len(queue_bak) == 0: break
            rev_flag = not rev_flag
            queue = queue_bak
            queue_bak = collections.deque([])

        return res