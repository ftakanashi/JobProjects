#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution1:
    def longestPalindrome(self, s: str) -> str:
        ans = ''
        n = len(s)

        def scan(left, right, ans):
            # 从给定的起始边界向两侧扫描
            while left >= 0 and right < n and s[left] == s[right]:
                left -= 1
                right += 1
            left, right = left + 1, right - 1
            if right - left + 1 > len(ans):
                ans = s[left:right + 1]
            return ans

        for i in range(n):
            ans = scan(i - 1, i + 1, ans)
            ans = scan(i, i + 1, ans)

        return ans

class Solution2:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]
        ans = ''
        for l in range(n):
            for i in range(n):
                j = i + l
                if j >= n: break
                if l == 0:
                    dp[i][j] = True
                elif l == 1:
                    dp[i][j] = (s[i] == s[j])
                elif dp[i+1][j-1] and s[i] == s[j]:
                    dp[i][j] = True

                if dp[i][j] and l + 1 > len(ans):
                    ans = s[i:j+1]

        return ans