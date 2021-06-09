#!/usr/bin/env python
from typing import List

from collections import Counter
from functools import lru_cache as cache

class Solution:
    def minChanges(self, nums: List[int], k: int) -> int:
        # 每列的counter
        counters = [Counter() for _ in range(k)]
        for i, num in enumerate(nums):
            counters[i % k][num] += 1

        # 每列的众数频数
        commons = [counter.most_common(1)[0][1] for counter in counters]

        ans = len(nums) - sum(commons)    # 将每列数字都改成众数的代价总和，也是基准值

        @cache
        def dfs(start, cur_xor):
            if start == k:
                return 0 if cur_xor == 0 else float('inf')

            res = float('inf')

            # 将列中数字全改成列中某数字后，使得最终异或结果为零的最小操作次数
            counter = counters[start]
            for num in sorted(counter.keys(), reverse=True, key=lambda x: counter[x]):    # 为了让尽量小的额外代价尽快出现，设置遍历顺序
                extra = commons[start] - counter[num]    # 改成数字num时引发的额外代价
                if extra >= res: continue
                res = min(res, dfs(start+1, cur_xor^num) + extra)

            # 将列中数字全改成非列中某数字的情况，因为改成什么数字完全是自由的，可以证明这么做一定能够达成最终目标
            # 因此，也就是说，对于某列数字的dfs，结果最大最大也不过是这列数字众数的频数（改成非列中数字的额外代价，就是将所有众数也改了，所以是众数频数而非列元素总数）
            res = min(res, commons[start])

            return res

        return ans + dfs(0, 0)