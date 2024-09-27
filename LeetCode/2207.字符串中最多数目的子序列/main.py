#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def maximumSubsequenceCount(self, text: str, pattern: str) -> int:
        c1, c2 = pattern

        # 特殊情况
        if c1 == c2:
            cnt = text.count(c1) + 1
            return (cnt - 1) * cnt // 2

        # 普通情况，一次遍历并计数 pattern 中两个字母出现的频次
        ans = cnt1 = cnt2 = 0
        for ch in text:
            if ch == c1:
                cnt1 += 1
            elif ch == c2:
                ans += cnt1
                cnt2 += 1

        return ans + max(cnt1, cnt2)