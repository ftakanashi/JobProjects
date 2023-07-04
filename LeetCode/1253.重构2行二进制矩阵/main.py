#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def reconstructMatrix(self, upper: int, lower: int, colsum: List[int]) -> List[List[int]]:
        n = len(colsum)
        ans = [[0 for _ in range(n)] for _ in range(2)]

        for i in range(n):

            # 2的情况
            if colsum[i] == 2:
                ans[0][i], ans[1][i] = 1, 1
                upper -= 1
                lower -= 1

            # 1的情况
            elif colsum[i] == 1:
                if upper >= lower:
                    ans[0][i] = 1
                    upper -= 1
                else:
                    ans[1][i] = 1
                    lower -= 1

            # 0的情况什么都不用做，所以没有特地写个分支

            if upper < 0 or lower < 0: return []

        return ans if upper == 0 and lower == 0 else []