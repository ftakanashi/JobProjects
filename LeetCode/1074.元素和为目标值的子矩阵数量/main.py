#!/usr/bin/env python
from typing import List

from collections import Counter

class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        m, n = len(matrix), len(matrix[0])
        presum = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                presum[i][j] = matrix[i-1][j-1] + presum[i-1][j]

        def process(i1, i2):
            cnt = s = 0
            counter = Counter([0, ])
            for j in range(1, n+1):
                s += presum[i2][j] - presum[i1-1][j]
                if s - target in counter: cnt += counter[s - target]
                counter[s] += 1
            return cnt

        res = 0
        for i1 in range(1, m+1):
            for i2 in range(i1, m+1):
                res += process(i1, i2)
        return res