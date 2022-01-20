#!/usr/bin/env python

# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None

class Solution:
    def inorderSuccessor(self, node: 'Node') -> 'Optional[Node]':
        if node.right is None:
            # 输入节点右子树为空，则可能的答案需要向上回溯
            while node.parent is not None and node.parent.right is node:
                node = node.parent
            return node.parent    # 此时node可能是根节点（说明输入节点是整个BST的最大节点），返回None；也有可能是某个节点whose parent的左子树包含了输入节点
        else:
            # 输入右子树不为空，那就是类似于迭代遍历树时的"左到底"了
            ans = node.right
            while ans.left is not None:
                ans = ans.left
            return ans