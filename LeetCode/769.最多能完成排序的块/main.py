#!/usr/bin/env python
from typing import List

class Solution1:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        set1, set2 = set(), set()
        count = 0
        for i, n in enumerate(arr):
            set1.add(i)
            set2.add(n)
            if set1 == set2:
                set1.clear(), set2.clear()
                count += 1
        return count

class Solution2:
    def maxChunksToSorted(self, arr):
        count, max_a = 0, 0
        for i, n in enumerate(arr):
            max_a = max(max_a, n)
            if max_a == i: count += 1
        return count