#!/usr/bin/env python
from collections import Counter
class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        ans = 0
        has_odd = False
        for ch, times in counter.items():
            if times & 1 == 0:
                ans += times
            else:
                has_odd = True
                ans += times - 1
        if has_odd: ans += 1
        return ans