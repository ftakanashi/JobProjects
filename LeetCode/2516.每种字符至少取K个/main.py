#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import Counter

class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        cnt = Counter(s)
        if min(cnt['a'], cnt['b'], cnt['c']) < k:
            return -1

        l = r = 0
        ans = len(s)
        while r < len(s):
            cnt[s[r]] -= 1

            while min(cnt['a'], cnt['b'], cnt['c']) < k and l < r:
                cnt[s[l]] += 1
                l += 1

            if min(cnt['a'], cnt['b'], cnt['c']) >= k:
                ans = min(ans, len(s) - (r - l + 1))

            r += 1

        return ans