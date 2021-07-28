#!/usr/bin/env python
from typing import List

class Solution1:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        covered = set()
        for a, b in ranges:
            for num in range(a, b+1):
                covered.add(num)

        for num in range(left, right+1):
            if num not in covered: return False
        return True

class Solution2:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        diff = [0 for _ in range(52)]
        for a, b in ranges:
            diff[a] += 1
            diff[b+1] -= 1

        s = 0
        for i in range(len(diff)):
            s += diff[i]
            if left <= i <= right and s <= 0: return False
        return True