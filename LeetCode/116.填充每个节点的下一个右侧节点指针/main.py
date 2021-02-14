#!/usr/bin/env python
import collections

# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution1:
    def connect(self, root: 'Node') -> 'Node':
        if not root: return
        queue = collections.deque([])
        queue.append(root)
        while queue:
            q_len = len(queue)
            i = 0
            while i < q_len - 1:
                queue[i].next = queue[i + 1]
                i += 1
            for _ in range(q_len):
                node = queue.popleft()
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
        return root

class Solution2:
    def connect(self, root: 'Node') -> 'Node':

        def rec(node):
            if node is None or node.left is None and node.right is None:
                return
            node.left.next = node.right
            if node.next is not None:
                node.right.next = node.next.left
            rec(node.left)
            rec(node.right)

        rec(root)
        return root