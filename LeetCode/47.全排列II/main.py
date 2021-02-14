#!/usr/bin/env python
from typing import List

class Solution1:
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

class Solution2:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        def dfs(pos: int):
            if pos == n - 1:
                res.append(nums.copy())
                return
            seen = set()
            for i in range(pos, n):
                if nums[i] in seen: continue
                seen.add(nums[i])
                nums[pos], nums[i] = nums[i], nums[pos]
                dfs(pos + 1)
                nums[pos], nums[i] = nums[i], nums[pos]

        dfs(0)
        return res