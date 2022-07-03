#!/usr/bin/env python
from typing import List

class Solution:
    def isBoomerang(self, points: List[List[int]]) -> bool:
        a, b, c = points
        if a == b or a == c or b == c: return False
        k1 = (a[1] - b[1]) / (a[0] - b[0]) if a[0] - b[0] != 0 else None
        k2 = (b[1] - c[1]) / (b[0] - c[0]) if b[0] - c[0] != 0 else None
        return k1 != k2