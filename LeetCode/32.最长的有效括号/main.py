#!/usr/bin/env python

class Solution1:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1: return 0
        stack = []
        ans = 0
        for i in range(len(s)):
            if stack and s[stack[-1]] == '(' and s[i] == ')':
                stack.pop()
                ans = max(ans, (i - stack[-1]) if stack else (i + 1))
            else:
                stack.append(i)
        return ans

class Solution2:
    def longestValidParentheses(self, s: str) -> int:
        if len(s) <= 1: return 0
        dp = [0 for _ in range(len(s))]
        dp[1] = 2 if s[:2] == '()' else 0

        for i in range(2, len(s)):
            if s[i] == ')':
                if s[i-1] == '(':
                    dp[i] = dp[i-2] + 2
                elif i - dp[i-1] - 1 >= 0 and s[i - dp[i-1] - 1] == '(':
                    dp[i] = dp[i-1] + 2
                    if i - dp[i-1] - 2 >= 0:
                        dp[i] += dp[i - dp[i-1] - 2]

        return max(dp)