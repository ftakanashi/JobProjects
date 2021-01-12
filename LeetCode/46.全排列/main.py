#!/usr/bin/env python
from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        def rec(i: int) -> List[List[int]]:
            if i == n - 1:
                return [[nums[n-1], ]]

            res = []
            for subset in rec(i + 1):
                for pos in range(len(subset) + 1):
                    subset.insert(pos, nums[i])    # 插入
                    res.append(subset.copy())    # 一定要有copy
                    del subset[pos]    # 为了后面的操作还原
            return res

        return rec(0)