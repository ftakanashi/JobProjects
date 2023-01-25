#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

import math
class Solution:
    def bestCoordinate(self, towers: List[List[int]], radius: int) -> List[int]:
        max_x, max_y = 0, 0
        for x, y, _ in towers:
            max_x = max(max_x, x)
            max_y = max(max_y, y)

        def calc_quality(pos):
            x, y = pos
            quality = 0
            for tx, ty, q in towers:
                dist = math.sqrt((tx - x) ** 2 + (ty - y) ** 2)
                if dist > radius: continue
                quality += math.floor(q / (1 + dist))
            return quality

        max_quality = 0
        ans = [0, 0]
        for i in range(max_x + 1):
            for j in range(max_y + 1):
                quality = calc_quality((i, j))
                if quality > max_quality:
                    ans = [i, j]
                    max_quality = quality
        return ans