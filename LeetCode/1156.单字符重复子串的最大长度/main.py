#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import Counter

class Solution:
    def maxRepOpt1(self, text: str) -> int:
        n = len(text)
        counter = Counter(text)
        i = ans = 0

        while i < n:
            ch = text[i]

            # 扫描第一片a
            j = i
            while j < n and text[j] == ch:
                j += 1

            # 基于第一片a，统计答案
            span = j - i
            if span < counter[ch]:
                ans = max(ans, span + 1)
            elif span == counter[ch]:
                ans = max(ans, span)

            # 扫描第二片a
            k = j + 1
            while k < n and text[k] == ch:
                k += 1

            # 基于第二片a，统计答案
            if k - i - 1 < counter[ch]:
                ans = max(ans, k - i)
            elif k - i - 1 == counter[ch]:
                ans = max(ans, k - i - 1)

            i = j

        return ans