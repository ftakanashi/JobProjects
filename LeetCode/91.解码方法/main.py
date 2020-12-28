#!/usr/bin/env python

class Solution:
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