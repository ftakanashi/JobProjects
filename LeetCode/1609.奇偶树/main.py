#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

import collections
class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        # 初始化队列和其他变量
        queue = collections.deque([root])
        level = 0
        switch = 1

        while len(queue) > 0:

            prev = switch * -float('inf')    # 判递增还是递减的前序变量
            for _ in range(len(queue)):
                # 处理节点次数不超过本层节点个数
                node = queue.popleft()

                # 两个条件的判断
                if (node.val & 1) ^ (level & 1) == 0 or \
                        (node.val - prev) * switch <= 0:
                    return False

                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
                prev = node.val

            # 上面for循环结束时，保证当前层的节点已经处理完成且队列中
            # 所有下一层的子节点都已经入队。此时更新level和switch，进行下一轮循环
            level += 1
            switch *= -1

            # 如果此时queue为空，表明下一层所有子节点都是None，或者说根本没有子节点，说明来到最后一层
            # 因此可以直接跳出。

        return True