#!/usr/bin/env python
from typing import List

class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        source = [0, 0]

        def dist(point1, point2):
            return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

        d = dist(source, target)
        return all(dist(ghost, target) > d for ghost in ghosts)