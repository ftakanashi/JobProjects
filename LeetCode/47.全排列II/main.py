#!/usr/bin/env python
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        counter = {}
        for num in nums:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1

        res = []
        def rec(seq: List[int], counter: dict):
            if len(seq) == n:
                res.append(seq)
            for num in counter:
                if counter[num] == 0: continue
                counter[num] -= 1
                seq.append(num)
                rec(seq.copy(), counter.copy())
                seq.pop()
                counter[num] += 1

        rec([], counter)
        return res