#!/usr/bin/env python
# -*- coding:utf-8 -*-

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution1:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        if root.left is None and root.right is None:
            return 1

        left = self.countNodes(root.left)
        right = self.countNodes(root.right)
        return left + right + 1


import collections
class Solution2:
    def countNodes(self, root: TreeNode) -> int:
        if root is None:
            return 0
        queue = collections.deque()
        queue.append(root)
        count = 0
        while len(queue) > 0:
            node = queue.popleft()
            count += 1
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
        return count


class Solution3:
    def countNodes(self, root: TreeNode) -> int:
        if root is None: return 0
        h = 0    # 层数

        # 确定总层数
        node = root
        while node.left is not None:
            node = node.left
            h += 1

        # 确定最下层探索总节点个数的边界
        min_v = 2 ** h
        max_v = 2 ** (h+1) - 1

        # 二分查找
        while min_v < max_v:
            mid = int((max_v - min_v + 1) / 2) + min_v
            if self.exists(root, mid, h):
                min_v = mid
            else:
                max_v = mid - 1
        return min_v

    def exists(self, root, n, h):
        '''
        利用完全二叉树路径和节点序数二进制间的关系
        判断某个节点是否存在于树中
        '''
        node = root
        n -= (1 << h)    # 取出开头的1
        h -= 1
        while h >= 0:
            # 模拟从root开始往下探索目标节点。因为是完全二叉树，在h小于0前不用担心node变成None
            if n & (1 << h) == 0:
                node = node.left
            else:
                node = node.right
            h -= 1

        return node is not None