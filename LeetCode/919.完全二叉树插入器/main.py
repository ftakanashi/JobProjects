#!/usr/bin/env python

from collections import deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root
        self.tail_q = deque([root, ])
        while self.tail_q:
            node = self.tail_q.popleft()
            if node.left:
                self.tail_q.append(node.left)
            if node.right:
                self.tail_q.append(node.right)
            if node.right is None:
                self.tail = node
                break

    def insert(self, val: int) -> int:
        new_node = TreeNode(val)
        self.tail_q.append(new_node)
        if self.tail.left is None:
            self.tail.left = new_node
            return self.tail.val
        else:
            self.tail.right = new_node
            tmp = self.tail.val
            self.tail = self.tail_q.popleft()
            return tmp

    def get_root(self) -> TreeNode:
        return self.root

# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()