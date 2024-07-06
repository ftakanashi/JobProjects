#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

from collections import Counter
class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        l = r = 0
        cnt = Counter()
        while r < n:
            # 在字符串相同时获取尽可能长的特殊字符串，即尽可能拓展右边界
            while r < n and s[l] == s[r]:
                r += 1

            # 解析其带来的所有可能的特殊字符串
            ch = s[l]
            p = r - l
            for k in range(p):
                cnt[ch * (k + 1)] += (p - k)

            # 左边界直接跳过去
            l = r

        for ans in sorted(filter(lambda t: t[1] >= 3, cnt.items()), key=lambda t: len(t[0]), reverse=True):
            return len(ans[0])
        return -1