#!/usr/bin/env python
from typing import List

class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        wind_len = n - k
        i, j = 0, wind_len - 1
        total = sum(cardPoints[j+1:])
        max_total = total
        while True:
            j += 1
            if j == n: break
            total -= cardPoints[j]
            total += cardPoints[i]
            max_total = max(max_total, total)
            i += 1
        return max_total