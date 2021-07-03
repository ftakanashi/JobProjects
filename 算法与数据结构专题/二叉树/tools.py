#!/usr/bin/env python

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        s = f'[{self.val}'
        if self.left:
            s += f',L: {self.left}'
        if self.right:
            s += f',R: {self.right}'
        s += ']'
        return s

    def __repr__(self):
        return f'{self.val}'

import collections
def buildTree(lst):
    if len(lst) == 0: return
    root = TreeNode(lst[0])
    queue = collections.deque([root,])
    for i in range(1, len(lst), 2):
        node = queue.popleft()
        if lst[i]:
            left = TreeNode(lst[i])
            node.left = left
            queue.append(left)
        if i+1 < len(lst) and lst[i+1]:
            right = TreeNode(lst[i+1])
            node.right = right
            queue.append(right)

    return root

def printTree(root: TreeNode):
    res = []
    if not root: return res
    queue = collections.deque([root,])
    while queue:
        node = queue.popleft()
        res.append(node.val if node else None)
        if node and (node.left or node.right):
            queue.append(node.left)
            queue.append(node.right)
    return res


if __name__ == '__main__':
    t = buildTree([1,2,3,4,5,6,None,7,None,8,9])
    print(printTree(t))