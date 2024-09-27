#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import Counter
class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:
        nums = list(map(str, nums))
        n = len(nums[0])
        ans = 0
        for i in range(n):
            cnt = Counter([s[i] for s in nums])
            if len(cnt) <= 1: continue

            res = 0    # 计算当前数位，其总共可以贡献多少
            cnts = cnt.values()
            total = sum(cnts)
            for c in cnts:
                res += ((total - c) * c)
            res //= 2

            ans += res

        return ans