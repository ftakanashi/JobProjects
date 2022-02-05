#!/usr/bin/env python
from typing import List

class Solution:
    def minDistance(self, height: int, width: int, tree: List[int], squirrel: List[int], nuts: List[List[int]]) -> int:

        def dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def init_dist(p):    # 计算各个坚果的优越性，注意这里是 起点-坚果距离 减去 树-坚果距离，因此越小越优越
            return dist(squirrel, p) - dist(tree, p)

        first = min(nuts, key=lambda x:init_dist(x))    # 找到最优越的坚果作为去拿的第一个坚果
        total_dist = dist(first, squirrel) + dist(first, tree)
        for nut in nuts:
            if nut == first: continue
            total_dist += dist(nut, tree) * 2     # 将去拿剩余坚果的距离也累加进去
        return total_dist