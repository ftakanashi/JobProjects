#!/usr/bin/env python

class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        m, n = len(t), len(s)
        if n == 0 or m == 0 or n < m: return 0 if m > 0 else 1

        dp = [0 for _ in range(n)]
        tmp = 0
        for j in range(n):
            if s[j] == t[0]: tmp += 1
            dp[j] = tmp

        for i in range(1, m):
            prev = dp[i - 1]    # 别忘了每一行开始时即时更新这个量
            for j in range(i, n):
                if t[i] == s[j]:
                    fac = dp[j-1] if j > i else 0
                    tmp = dp[j]
                    dp[j] = prev + fac
                    prev = tmp
                else:
                    prev = dp[j]
                    dp[j] = dp[j-1] if j > i else 0
        return dp[-1]

        # dp = [[0 for _ in range(n)] for _ in range(m)]

        # tmp = 0
        # for j in range(n):
        #     if s[j] == t[0]: tmp += 1
        #     dp[0][j] = tmp

        # for i in range(1, m):
        #     for j in range(i, n):
        #         if t[i] != s[j]:
        #             dp[i][j] = dp[i][j - 1]
        #         else:
        #             dp[i][j] = dp[i][j-1] + dp[i-1][j-1]

        # return dp[-1][-1]
