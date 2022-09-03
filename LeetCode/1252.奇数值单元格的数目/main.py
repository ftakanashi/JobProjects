#!/usr/bin/env python
from typing import List


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = [0 for _ in range(m)]
        cols = [0 for _ in range(n)]
        for x, y in indices:
            rows[x] += 1
            cols[y] += 1

        ans = 0
        for i in range(m):
            for j in range(n):
                val = rows[i] + cols[j]
                if val & 1 == 1:
                    ans += 1
        return ans