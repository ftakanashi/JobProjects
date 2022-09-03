#!/usr/bin/env python
from typing import List

from collections import Counter
class Solution:
    def maxEqualFreq(self, nums: List[int]) -> int:
        counter = Counter()
        count_freq = Counter()
        ans = None
        for i, num in enumerate(nums):

            if count_freq[counter[num]] > 0:    # 别忘了要将之前的计数出现频率减去1。
                # 当然若原本是计数值0，因为后面的分支判断依赖于 len(count_freq)，容易引起混乱，所以选择不处理
                count_freq[counter[num]] -= 1
                if count_freq[counter[num]] == 0: count_freq.pop(counter[num])

            counter[num] += 1
            count_freq[counter[num]] += 1

            if len(count_freq) == 2:    # 只有当count_freq的长度为2，即出现过的计数值只有两种时才可能符合题意
                (c1, f1), (c2, f2) = sorted(count_freq.items())
                if c1 == 1 and f1 == 1:
                    ans = i + 1
                elif c2 - c1 == 1 and f2 == 1:
                    ans = i + 1

        return ans if ans is not None else len(nums)