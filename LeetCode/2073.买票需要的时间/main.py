#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        ans = 0
        p = tickets[k]
        for i, t in enumerate(tickets):
            if i <= k:
                ans += min(p, t)
            else:
                ans += min(p - 1, t)
        return ans
