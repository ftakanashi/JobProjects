#!/usr/bin/env python

class Solution:
    def binaryGap(self, n: int) -> int:
        s = bin(n)[2:]
        prev = ans = 0    # 保证s[0]肯定是1
        for i in range(1, len(s)):
            if s[i] == "1":
                ans = max(ans, i - prev)
                prev = i
        return ans