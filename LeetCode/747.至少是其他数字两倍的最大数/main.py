#!/usr/bin/env python
from typing import List

class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        _max = (-1, float('-inf'))
        _sec = (-1, float('-inf'))
        for i, num in enumerate(nums):
            if num > _max[1]:
                _sec = _max
                _max = (i, num)
            elif num > _sec[1]:
                _sec = (i, num)

        if _sec[1] == float('-inf') or _max[1] >= _sec[1] * 2:
            return _max[0]
        else:
            return -1