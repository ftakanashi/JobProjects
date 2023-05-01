#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def numMovesStones(self, a: int, b: int, c: int) -> List[int]:
        x, y, z = sorted([a, b, c])
        max_cnt = z - x - 2
        if y - x == 1 and z - y == 1:
            min_cnt = 0
        elif z - y in (1, 2) or y - x in (1, 2):
            min_cnt = 1
        else:
            min_cnt = 2

        return [min_cnt, max_cnt]