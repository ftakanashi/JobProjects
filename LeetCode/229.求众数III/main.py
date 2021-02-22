#!/usr/bin/env python

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        ths = len(nums) // 3
        mini_counter = {}
        for n in nums:
            if n in mini_counter:
                mini_counter[n] += 1
            elif len(mini_counter) < 2:
                mini_counter[n] = 1
            else:
                a, b = list(mini_counter.keys())
                mini_counter[a] -= 1
                mini_counter[b] -= 1
                if mini_counter[a] == 0: mini_counter.pop(a)
                if mini_counter[b] == 0: mini_counter.pop(b)

        res = list(mini_counter.keys())

        for ans in res:
            count = 0
            for n in nums:
                if ans == n: count += 1
            if count <= ths: res.remove(ans)

        return res