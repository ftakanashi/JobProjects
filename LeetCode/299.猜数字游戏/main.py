#!/usr/bin/env python
from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        count_s = defaultdict(int)
        count_g = defaultdict(int)
        n = len(secret)
        bull = cow = 0
        for i in range(n):
            if secret[i] == guess[i]:
                bull += 1
            else:
                count_s[secret[i]] += 1
                count_g[guess[i]] += 1

        for ch in count_g:
            cow += min(count_g[ch], count_s[ch])

        return f'{bull}A{cow}B'