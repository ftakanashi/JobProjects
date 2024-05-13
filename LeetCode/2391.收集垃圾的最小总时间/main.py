#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        travel = [0] + travel
        ans = sum(map(len, garbage)) + sum(travel) * 3

        for ch in "MPG":
            for i in range(len(garbage) - 1, -1, -1):
                if ch in garbage[i]:
                    break
                ans -= travel[i]

        return ans