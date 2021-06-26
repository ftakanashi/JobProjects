#!/usr/bin/env python
from typing import List

from collections import Counter

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        counter = Counter(answers)
        ans = 0
        for k, v in counter.items():
            if v % (k+1) == 0: ans += v
            else: ans += (k+1) * (v // (k+1) + 1)
        return ans