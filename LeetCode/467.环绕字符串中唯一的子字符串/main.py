#!/usr/bin/env python
import string


class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        n = len(p)
        dp = {ch: 1 for ch in string.ascii_lowercase}
        length = 1
        for i in range(1, n):
            if (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                length += 1
                dp[p[i]] = max(length, dp[p[i]])
            else:
                length = 1

        ans = 0
        for ch in set(p):
            ans += dp[ch]
        return ans