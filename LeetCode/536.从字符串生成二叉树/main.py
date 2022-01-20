#!/usr/bin/env python

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def str2tree(self, s: str) -> TreeNode:
        if s == "": return None
        if "(" not in s and ")" not in s: return TreeNode(val=int(s))

        stack = []
        i, n = 0, len(s)
        num = ""
        while i < n:
            if s[i] == "(":
                if num:
                    node = TreeNode(val=int(num))
                    stack.append(node)
                    num = ""
            elif s[i] == ")":
                if num:
                    node = TreeNode(val=int(num))
                    num = ""
                else:
                    node = stack.pop()
                prev = stack[-1]
                if prev.left is None:
                    prev.left = node
                else:
                    prev.right = node
            else:
                num += s[i]
            i += 1

        return stack[0]