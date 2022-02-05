#!/usr/bin/env python
from typing import List

from collections import Counter
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        ans = 0
        if k == 0:    # 如果 k == 0，那么就是针对所有数字计数，然后统计有多少数字的计数大于1（只要有超过1个，就能形成一个对
            counter = Counter(nums)
            for k in counter:
                if counter[k] > 1:
                    ans += 1
            return ans
        nums = list(set(nums))
        nums.sort()    # 去重后排序
        seen = set()
        for num in nums:
            if num - k in seen:
                ans += 1
            seen.add(num)
        return ans