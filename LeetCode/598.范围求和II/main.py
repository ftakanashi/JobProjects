#!/usr/bin/env python
from typing import List

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:
        if len(ops) == 0: return m * n
        min_a = min(op[0] for op in ops)
        min_b = min(op[1] for op in ops)
        return min_a * min_b