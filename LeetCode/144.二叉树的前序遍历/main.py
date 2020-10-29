#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution1:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []

        res = [root.val, ]
        res.extend(self.preorderTraversal(root.left))
        res.extend(self.preorderTraversal(root.right))

        return res


class Solution2:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        if root is None:
            return []

        stack = []
        stack.append(root)
        res = []
        while len(stack) > 0:
            # 只要栈还没空就继续处理
            node = stack.pop()
            res.append(node.val)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res


class Solution3:
    def preorderTraversal(self, root: TreeNode) -> List[int]:

        # 特殊情况处理
        if root is None:
            return []

        res = []
        p1 = root
        while p1:
            if p1.left is None:
                # 左子树为空，直接记录val并开始右子树处理
                res.append(p1.val)
                p1 = p1.right    # 当有回溯连接时，这里穿越的起点！！！
            else:
                p2 = p1.left
                while p2.right and p2.right != p1:
                    p2 = p2.right
                # 此时p2为左子树右下叶节点。
                # 在这个算法里，这种右下叶节点p2的右子树只有两种状态的可能
                # 1. None，说明当前处理的树的root节点即p1可以被收割并且开始处理其左子树。同时，为了让左子树处理完成后能够下一步继续处理右子树，把p2的右子连接连到p1上。相当于留一个回溯的路径。这页标志着p1左子树处理的开始。
                # 2. p1，如可能1中所说，当遍历到p2且其右子连接连在p1，标志着p1左子树处理的结束。那么就可以把当时新增的回溯连接拆掉，同时开始处理p1的右子树。
                # 整个算法还是用迭代模拟递归的味道

                if p2.right is None:  # 上面循环因为 p2.right is None 而跳出
                    p2.right = p1
                    res.append(p1.val)
                    p1 = p1.left

                else:  # 上面循环因为 p2.right == p1 而跳出
                    p2.right = None
                    p1 = p1.right

        return res
