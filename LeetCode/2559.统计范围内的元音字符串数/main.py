#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        # 构建前缀和数组
        is_vowel = [1 if (word[0] in "aeiou" and word[-1] in "aeiou") else 0 for word in words]
        presum = [0, ]
        for n in is_vowel:
            presum.append(presum[-1] + n)

        # 对每个query求解
        ans = []
        for l, r in queries:
            ans.append(presum[r + 1] - presum[l])
        return ans