#!/usr/bin/env python
from typing import List

from collections import Counter
from itertools import product

class Solution:
    def gridIllumination(self, n: int, lamps: List[List[int]], queries: List[List[int]]) -> List[int]:
        rows = Counter()
        cols = Counter()
        diag = Counter()
        revd = Counter()
        seen = set()
        for x, y in lamps:
            if (x, y) in seen: continue    # 别忘了题目说lamps中可能会有重复
            seen.add((x, y))
            rows[x] += 1
            cols[y] += 1
            diag[x + y] += 1
            revd[x - y] += 1

        ans = [0] * len(queries)
        direcs = list(product([-1, 0, 1], [-1, 0, 1]))
        for i, (qx, qy) in enumerate(queries):
            if rows[qx] > 0 or cols[qy] > 0 or diag[qx + qy] > 0 or revd[qx - qy] > 0:
                ans[i] = 1

            for a, b in direcs:
                nx, ny = qx + a, qy + b
                if (nx, ny) in seen:    # 若某个query位置附近九宫格内有已经点亮的灯
                    ans[i] = 1    # 本位置当前是被照亮的
                    # 将该亮灯熄灭
                    seen.remove((nx, ny))
                    rows[nx] -= 1
                    cols[ny] -= 1
                    diag[nx + ny] -= 1
                    revd[nx - ny] -= 1
        return ans