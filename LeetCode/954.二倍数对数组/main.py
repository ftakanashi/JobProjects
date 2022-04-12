#!/usr/bin/env python
from typing import List
from collections import Counter

class Solution:
    def canReorderDoubled(self, arr: List[int]) -> bool:
        counter = Counter(arr)
        if counter[0] & 1 == 1: return False
        for num in sorted(counter, key=abs):
            if num == 0: continue
            if counter[num * 2] >= counter[num]:
                counter[num * 2] -= counter[num]
            else:
                return False

        return True