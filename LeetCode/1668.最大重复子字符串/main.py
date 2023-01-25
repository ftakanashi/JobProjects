#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        n, m = len(sequence), len(word)
        if n < m:
            return 0

        dp = [0 for _ in range(n)]
        for i in range(m - 1, n):
            if sequence[:i+1].endswith(word):
                dp[i] = 1 if i == m - 1 else (dp[i - m] + 1)

        return max(dp)