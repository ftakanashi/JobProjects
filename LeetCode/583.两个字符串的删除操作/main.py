#!/usr/bin/env python

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m, n = len(word1), len(word2)
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            ch1 = word1[i-1]
            for j in range(1, n+1):
                ch2 = word2[j-1]

                if ch1 == ch2:
                    dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1], dp[i-1][j-1]+1)
                else:
                    dp[i][j] = max(dp[i][j], dp[i-1][j], dp[i][j-1])

        lcs = dp[-1][-1]
        ans = (m - lcs) + (n - lcs)
        return ans