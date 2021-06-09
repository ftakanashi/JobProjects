#!/usr/bin/env python
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        s = res = 0
        counter = {0: 1}
        for num in nums:
            s += num    # 实时计算前缀和，别忘了我们要处理的前缀和数组而不是原数组
            if s - k in counter: res += counter[s - k]
            if s not in counter: counter[s] = 0
            counter[s] += 1

        return res