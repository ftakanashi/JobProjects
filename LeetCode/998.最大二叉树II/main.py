#!/usr/bin/env python
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def insertIntoMaxTree(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        dummy = TreeNode(-1)
        dummy.right = root
        prev, node = dummy, root
        new = TreeNode(val)
        while node is not None:
            if node.val > val:    # 扫描过程中，若节点的值大于新插入值，则继续向右子树扫描
                prev = node
                node = node.right
            else:     # 否则 打断当前链接，将新节点插入到这个位置
                prev.right = new
                new.left = node
                break
        if node is None:
            prev.right = new

        return dummy.right