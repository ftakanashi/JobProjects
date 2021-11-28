#!/usr/bin/env python
from typing import List

class Solution:
    def maxProduct(self, words: List[str]) -> int:
        ans = 0
        words.sort(key=lambda x:len(x), reverse=True)
        n = len(words)
        flags = [0 for _ in range(n)]
        for i, word in enumerate(words):
            f = 0
            for ch in word:
                f |= (1 << (ord(ch) - ord('a')))
            flags[i] = f

        for i in range(n):
            for j in range(i):
                if flags[i] & flags[j] > 0: continue
                cur = len(words[i]) * len(words[j])
                if cur < ans: break
                else: ans = max(ans, len(words[i]) * len(words[j]))
        return ans