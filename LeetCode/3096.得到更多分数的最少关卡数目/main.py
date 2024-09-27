#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minimumLevels(self, possible: List[int]) -> int:
        presum = [0, ]
        s = 0

        for num in possible:
            s += 1 if num > 0 else -1
            presum.append(s)

        for i in range(len(possible) - 1):
            if presum[i + 1] > presum[-1] // 2:
                return i + 1
        return -1
