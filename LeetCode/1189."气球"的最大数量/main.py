#!/usr/bin/env python

from collections import Counter
class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        std = {"b": 1, "a": 1, "l": 2, "o": 2, "n": 1}
        counter = Counter()
        for ch in text:
            if ch in std:
                counter[ch] += 1

        ans = float("inf")
        for ch in std:
            ans = min(ans, counter[ch] // std[ch])
        return ans