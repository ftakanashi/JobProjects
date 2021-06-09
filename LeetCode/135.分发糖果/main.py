#!/usr/bin/env python
from typing import List

class Solution:
    def candy(self, ratings: List[int]) -> int:
        n, stack, l = len(ratings), [], 0
        res = [1 for _ in range(n)]
        for i in range(n-1, -1, -1):
            while stack and ratings[i] <= stack[-1]:
                stack.pop()
                l = 0
            l += 1
            res[i] = l
            stack.append(ratings[i])

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                res[i] = max(res[i-1] + 1, res[i])

        return sum(res)