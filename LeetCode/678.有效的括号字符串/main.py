#!/usr/bin/env python

class Solution1:
    def checkValidString(self, s: str) -> bool:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]

        for i in range(n):
            if s[i] == '*':
                dp[i][i] = True

        for i in range(n):
            if s[i:i+2] in ('()','*)','(*','**'):
                dp[i][i+1] = True

        for l in range(2, n):
            for i in range(n):
                j = i + l
                if j >= n: break
                if s[j] == '(': continue

                dp[i][j] = dp[i][j] or (dp[i+1][j-1] and s[i] in '*(')

                for k in range(i+1, j):
                    dp[i][j] = dp[i][j] or (dp[i][k-1] and dp[k][j])

        return dp[0][-1]

class Solution2:
    def checkValidString(self, s: str) -> bool:
        min_v = max_v = 0
        for ch in s:
            if ch == '(':
                min_v += 1
                max_v += 1
            elif ch == ')':
                min_v -= 1
                max_v -= 1
            else:
                min_v -= 1
                max_v += 1
            if max_v < 0: return False
            if min_v < 0: min_v = 0

        return min_v == 0