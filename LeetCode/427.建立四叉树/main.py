#!/usr/bin/env python
from typing import List

# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':

        def rec(top, bottom, left, right):
            if top == bottom and left == right:
                # 递归终止条件：当前探索区域是一个边长为1的正方形
                val = grid[top][left]
                return Node(val, True, None, None, None, None)

            mid_x, mid_y = (top + bottom) // 2, (left + right) // 2
            top_left = rec(top, mid_x, left, mid_y)
            top_right = rec(top, mid_x, mid_y + 1, right)
            bottom_left = rec(mid_x + 1, bottom, left, mid_y)
            bottom_right = rec(mid_x + 1, bottom, mid_y + 1, right)
            if top_left.val == top_right.val == bottom_left.val == bottom_right.val and all(
                    (top_left.isLeaf, top_right.isLeaf, bottom_left.isLeaf, bottom_right.isLeaf)):
                # 叶子节点可以递归收缩的情况
                node = Node(top_left.val, True, None, None, None, None)
            else:
                node = Node(1, False, top_left, top_right, bottom_left, bottom_right)
            return node

        n = len(grid)
        return rec(0, n - 1, 0, n - 1)