#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

import bisect

class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        presum = [0, ]
        for num in nums:
            presum.append(presum[-1] + num)

        presum = presum[1:]
        ans = []
        for q in queries:
            ans.append(bisect.bisect(presum, q))
        return ans