# -*- coding:utf-8 -*-

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

def preorder(root: TreeNode):
    if root is None: return []
    stack = [root, ]
    res = []
    while stack:
        node = stack.pop()
        res.append(node.val)
        if node.right: stack.append(node.right)
        if node.left: stack.append(node.left)
    return res

def midorder(root: TreeNode):
    if root is None: return []
    stack = []
    res = []
    while stack:
        while root:
            stack.append(root)
            root = root.left
        node = stack.pop()
        res.append(node)
        root = node.right