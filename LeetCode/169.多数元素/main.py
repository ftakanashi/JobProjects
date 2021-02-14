#!/usr/bin/env python
from typing import List

class Solution1:
    def majorityElement(self, nums: List[int]) -> int:
        counter = {}
        for n in nums:
            if n not in counter: counter[n] = 0
            counter[n] += 1
        max_c = -1
        res = None
        for n, count in counter.items():
            if count > max_c:
                max_c = count
                res = n
        return res

class Solution2:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = count = 0
        for n in nums:
            if count == 0:
                candidate = n
                count = 1
            elif n == candidate:
                count += 1
            else:
                count -= 1

        return candidate