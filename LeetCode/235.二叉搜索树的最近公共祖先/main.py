#!/usr/bin/env python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        i = root
        while True:
            if p.val < i.val: next_p = i.left
            elif p.val > i.val: next_p = i.right
            else: next_p = i

            if q.val < i.val: next_q = i.left
            elif q.val > i.val: next_q = i.right
            else: next_q = i

            if next_p != next_q:
                return i
            i = next_p