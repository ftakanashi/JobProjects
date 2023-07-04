#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        max_pos = ans = 0
        for i, pos in enumerate(flips):
            max_pos = max(max_pos, pos)
            if i + 1 == max_pos:
                ans += 1
        return ans