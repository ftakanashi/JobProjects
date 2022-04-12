#!/usr/bin/env python
from typing import List

from collections import deque
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if root is None: return []
        queue = deque()
        queue.append(root)
        ans = []
        while queue:
            layer = []
            for _ in range(len(queue)):
                node = queue.popleft()
                layer.append(node.val)
                for child in node.children:
                    queue.append(child)
            ans.append(layer)
        return ans