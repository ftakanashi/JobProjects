#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import defaultdict, Counter

class Solution:
    def maximumLength(self, s: str) -> int:
        n = len(s)
        l = r = 0
        cnt = defaultdict(list)
        while r < n:
            while r < n and s[l] == s[r]:
                r += 1
            cnt[s[l]].append(r - l)
            l = r

        ans = -1
        for ch, spans in cnt.items():
            span_cnt = Counter(spans)
            for l in sorted(span_cnt, reverse=True):
                if span_cnt[l] >= 3:
                    ans = max(ans, l)
                elif span_cnt[l] == 2 or (span_cnt[l] == 1 and span_cnt[l-1] >= 1):
                    ans = max(ans, l - 1)
                if l > 2:
                    ans = max(ans, l - 2)

                if ans > 0: break

        return ans if ans > 0 else -1