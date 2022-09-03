#!/usr/bin/env python
from typing import Optional, List
from collections import Counter
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import uuid


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        node_map = {}
        counter = Counter()
        ans = []

        def dfs(node):
            if node is None: return

            flag = (node.val, dfs(node.left), dfs(node.right))
            if flag not in node_map:
                node_map[flag] = str(uuid.uuid4())

            uid = node_map[flag]
            counter[uid] += 1
            if counter[uid] == 2:
                ans.append(node)
            return uid

        dfs(root)
        return ans