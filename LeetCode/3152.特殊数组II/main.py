#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        flags = [0, ]
        for i in range(1, len(nums)):
            flags.append(flags[-1] + ((nums[i] & 1) ^ (nums[i - 1] & 1)))

        return [(flags[b] - flags[a]) == b - a for a, b in queries]