#!/usr/bin/env python

class Solution1:
    def numDecodings(self, s: str) -> int:
        if len(s) == 0: return 0

        mem = [None for _ in range(len(s))]    # 记忆体
        def dfs(n: int):
            if n >= len(s):
                return 1
            if mem[n] is not None: return mem[n]

            c1 = c2 = 0
            if s[n] != '0':
                c1 = dfs(n + 1)
                if n < len(s) - 1 and 0 < int(s[n:n+2]) < 27:
                    c2 = dfs(n + 2)
            mem[n] = c1 + c2
            return c1 + c2

        count = dfs(0)
        return count

class Solution2:
    def numDecodings(self, s: str) -> int:
        if s and s[0] == 0: return 0    # 注意如果一开始就是0，那么注定没有合法解析方式，直接返回0即可
        dp0 = dp1 = 1
        for i in range(1, len(s)):
            dp = 0
            if s[i] == '0':
                if s[i-1] in '12': dp += dp0
            else:
                if s[i-1] != '0' and int(s[i-1:i+1]) <= 26: dp += dp0
                dp += dp1
            dp0, dp1 = dp1, dp
        return dp1

        # dp = [0 for _ in range(len(s) + 1)]
        # dp[0] = 1
        # dp[1] = 1 if s[0] != '0' else 0
        # for i in range(2, len(s) + 1):
        #     ch, prev = s[i-1], s[i-2]
        #     if ch == '0':
        #         if prev in '12': dp[i] += dp[i-2]
        #     else:
        #         if prev != '0' and int(s[i-2:i]) <= 26: dp[i] += dp[i-2]
        #         dp[i] += dp[i-1]

        # return dp[-1]