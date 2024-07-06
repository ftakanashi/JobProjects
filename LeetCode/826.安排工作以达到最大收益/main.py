#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution1:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        m, n = len(worker), len(profit)
        items = list(zip(difficulty, profit))
        items.sort()

        _m, max_profit = -1, []
        for i in range(n):
            _m = max(_m, items[i][1])
            max_profit.append(_m)

        ans = 0
        for i in range(m):
            w = worker[i]
            l, r = 0, n - 1
            while l <= r:
                mid = (l + r) // 2
                if items[mid][0] > w:
                    r = mid - 1
                else:
                    l = mid + 1
            ans += (max_profit[r] if r >= 0 else 0)
        return ans

class Solution2:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        m, n = len(worker), len(profit)
        items = list(sorted(zip(difficulty, profit)))
        worker.sort()

        i = j = ans = max_p = 0
        while i < m:
            while j < n and worker[i] >= items[j][0]:
                max_p = max(max_p, items[j][1])
                j += 1
            ans += max_p
            i += 1

        return ans