#!/usr/bin/env python
from typing import List

class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if len(original) != m * n: return []
        ans = [[None for _ in range(n)] for _ in range(m)]

        for i, num in enumerate(original):
            ans[i // n][i % n] = num
        return ans