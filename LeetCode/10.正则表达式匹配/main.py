#!/usr/bin/env python

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m, n = len(p), len(s)
        dp = [[False for _ in range(n+1)] for _ in range(m+1)]
        dp[0][0] = True
        for i in range(1, m):
            if p[i] == '*':
                dp[i+1][0] = True
            elif p[i-1] != '*':
                break

        for i in range(1, m+1):
            for j in range(1, n+1):
                if p[i-1] != '*':
                    dp[i][j] = dp[i-1][j-1] and (p[i-1] == '.' or p[i-1] == s[j-1])
                else:
                    if dp[i][j-1] and (p[i-2] == '.' or p[i-2] == s[j-1]):
                        dp[i][j] = True
                    if i > 2 and dp[i-2][j]:
                        dp[i][j] = True

        return dp[-1][-1]