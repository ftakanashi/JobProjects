#!/usr/bin/env python

from typing import List

class Solution:
    def getMaxMatrix(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        res = [0, 0, 0, 0]
        max_sum = matrix[0][0]

        presum = [[0 for _ in range(n)] for _ in range(m)]
        presum[0] = matrix[0].copy()
        for i in range(1, m):
            for j in range(n):
                presum[i][j] = presum[i-1][j] + matrix[i][j]

        for i in range(m):
            for j in range(i, m):
                nums = presum[j].copy()
                if i > 0:
                    for k in range(n): nums[k] -= presum[i-1][k]

                dp = nums[0]
                s = e = 0
                for e in range(1, len(nums)):
                    num = nums[e]
                    if dp + num < num:
                        dp = num
                        s = e
                    else:
                        dp = dp + num

                    if dp > max_sum:
                        max_sum = dp
                        res = [i, s, j, e]

        return res