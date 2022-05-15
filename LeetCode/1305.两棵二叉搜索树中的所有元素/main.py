#!/usr/bin/env python
from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution1:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:

        def dfs(node, res_con):
            if node is None: return
            dfs(node.left, res_con)
            res_con.append(node.val)
            dfs(node.right, res_con)

        res1, res2 = [], []
        dfs(root1, res1)
        dfs(root2, res2)

        ans = []
        i = j = 0
        while i < len(res1) and j < len(res2):
            if res1[i] <= res2[j]:
                ans.append(res1[i])
                i += 1
            else:
                ans.append(res2[j])
                j += 1

        while i < len(res1):
            ans.append(res1[i])
            i += 1
        while j < len(res2):
            ans.append(res2[j])
            j += 1

        return ans


class Solution2:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        stack1, stack2 = [], []
        ans = []
        while (root1 or len(stack1) > 0) and (root2 or len(stack2) > 0):
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            if stack1[-1].val <= stack2[-1].val:
                root1 = stack1.pop()
                ans.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                ans.append(root2.val)
                root2 = root2.right

        while root1 or len(stack1) > 0:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            root1 = stack1.pop()
            ans.append(root1.val)
            root1 = root1.right

        while root2 or len(stack2) > 0:
            while root2:
                stack2.append(root2)
                root2 = root2.left
            root2 = stack2.pop()
            ans.append(root2.val)
            root2 = root2.right

        return ans
