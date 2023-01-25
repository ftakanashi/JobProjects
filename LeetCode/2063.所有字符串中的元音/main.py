#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution1:
    def countVowels(self, word: str) -> int:
        ans = 0
        for i, ch in enumerate(word):
            if ch in "aeiou":
                s_count = i + 1
                e_count = len(word) - i
                ans += (s_count * e_count)
        return ans

class Solution2:
    def countVowels(self, word):
        vowels, n = {"a", "e", "i", "o", "u"}, len(word)
        dp = [0] * n
        dp[0] = 1 if word[0] in vowels else 0
        # 理论上这里最好从2开始遍历，以避免i-2 < 0的情况。不过反正-1此时总是0，所以无所谓
        for i in range(1, n):
            if word[i] in vowels:
                dp[i] = 2 * dp[i-1] - dp[i-2] + i + 1
            else:
                dp[i] = 2 * dp[i-1] - dp[i-2]
        return dp[-1]