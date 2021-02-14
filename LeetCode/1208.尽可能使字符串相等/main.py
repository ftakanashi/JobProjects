#!/usr/bin/env python
class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        diff = []
        i = 0
        while i < len(s):
            diff.append(abs(ord(s[i]) - ord(t[i])))
            i += 1

        i, j = 0, 0
        total = 0
        max_len = 0
        while j < len(s):
            total += diff[j]
            while total > maxCost:
                total -= diff[i]
                i += 1
                if i == j: break    # 这行可以不要
            max_len = max(max_len, j - i + 1)
            j += 1
        return max_len