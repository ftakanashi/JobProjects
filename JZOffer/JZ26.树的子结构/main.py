#!/usr/bin/env python
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def contains(self, n1: TreeNode, n2: TreeNode) -> bool:
        if n1 is None: return n2 is None
        if n2 is None: return True
        if n1.val == n2.val:
            return self.contains(n1.left, n2.left) and self.contains(n1.right, n2.right)
        return False

    def isSubStructure(self, A: TreeNode, B: TreeNode) -> bool:

        if A is None or B is None: return False

        def dfs(node: TreeNode) -> bool:
            if node is None: return False
            if node.val == B.val and self.contains(node, B):
                # 当且仅当A某个子节点的值与B根节点相同且这个子树包含整个B，才能返回True，否则就要继续探索
                return True
            return dfs(node.left) or dfs(node.right)

        return dfs(A)