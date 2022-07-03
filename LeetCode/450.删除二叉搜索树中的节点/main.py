#!/usr/bin/env python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        dummy = TreeNode(float('inf'), root, None)

        def dfs(parent, node, direc):
            if node is None: return
            if key < node.val:
                dfs(node, node.left, "L")
            elif key > node.val:
                dfs(node, node.right, "R")
            elif node.left is None and node.right is None:    # 目标节点为叶子节点
                if direc == "L": parent.left = None
                else: parent.right = None
            elif node.right is None:    # 目标节点无右子树
                if direc == "L": parent.left = node.left
                else: parent.right = node.left
            elif node.right.left is None:    # 目标节点有右子树但其右子树无左子树
                node.val = node.right.val
                node.right = node.right.right
            else:    # 最后，目标节点有右子树且右子树有左子树
                prev, curr = node.right, node.right.left
                while curr.left:
                    prev = curr
                    curr = curr.left
                prev.left = curr.right
                node.val = curr.val

        dfs(dummy, root, "L")
        return dummy.left