#!/usr/bin/env python
from typing import List

class Solution1:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        mem = {}

        def dfs(start):
            if start == len(s): return True
            if start in mem: return mem[start]
            for end in range(start, len(s)):
                sub = s[start:end+1]
                if sub in word_set and dfs(end+1):
                    mem[start] = True
                    return True

            mem[start] = False
            return False

        return dfs(0)

class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        max_len = max([len(w) for w in wordDict])
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True
        for i in range(1, len(s) + 1):
            for j in range(max(0, i - max_len), i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True

        return dp[-1]