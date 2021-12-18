#!/usr/bin/env python
from collections import defaultdict

class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        l = r = max_len = 0
        window = defaultdict(int)
        while r < len(s):
            window[s[r]] += 1

            while len(window) > 2:
                window[s[l]] -= 1
                if window[s[l]] == 0:
                    window.pop(s[l])
                l += 1

            max_len = max(max_len, r - l + 1)
            r += 1
        return max_len