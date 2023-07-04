#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:

        # 构建异或前缀和数组
        presum = [0, ]
        for ch in s:
            val = 1 << (ord(ch) - ord('a'))
            presum.append(presum[-1] ^ val)

        ans = []
        for l, r, k in queries:
            # 基于异或前缀和数组快速确认片段中各个字母出现次数的奇偶性
            num = presum[r + 1] ^ presum[l]

            cnt = 0
            while num > 0:
                num = num & (num - 1)
                cnt += 1
            ans.append(cnt <= 2 * k + 1)

        return ans