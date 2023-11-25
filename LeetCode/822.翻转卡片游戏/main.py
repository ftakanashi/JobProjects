#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def flipgame(self, fronts: List[int], backs: List[int]) -> int:
        same = {f for f, b in zip(fronts, backs) if f == b}

        ans = float("inf")
        for num in fronts + backs:
            if num not in same:
                ans = min(ans, num)

        return 0 if ans == float("inf") else ans