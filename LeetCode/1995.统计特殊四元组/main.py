#!/usr/bin/env python
from typing import List

from collections import Counter
class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        counter = Counter()
        n = len(nums)
        ans = 0

        for b in range(n-3, 0, -1):    # 逆序扫描b，以b作为a,b和c,d之间的边界

            c = b + 1    # 提供一种新的可能的c为b+1，所有更大的c与d的差值在之前的扫描中都以统计过，不能重复统计
            for d in range(n-1, b+1, -1):
                counter[nums[d] - nums[c]] += 1

            for a in range(b):    # 统计 a + b
                if nums[a] + nums[b] in counter:
                    ans += counter[nums[a] + nums[b]]

        return ans