#!/usr/bin/env python

from typing import List
from collections import Counter
from functools import lru_cache as cache

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        counters = [Counter() for _ in range(k)]
        for i, num in enumerate(nums):
            counters[i % k][num] += 1

        commons = [counter.most_common(1)[0][1] for counter in counters]

        ans = len(nums) - sum(commons)

        @cache
        def dfs(start, cur_xor):
            if start == k:
                return 0 if cur_xor == 0 else float('inf')

            res = commons[start]
            counter = counters[start]
            for num in counter.keys():
                extra = commons[start] - counter[num]
                res = min(res, dfs(start+1, cur_xor^num) + extra)

            return res

        return ans + dfs(0, 0)

if __name__ == '__main__':
    s = Solution()
    res = s.minChanges([1,4,2,4,3,5] ,2)
    print(res)