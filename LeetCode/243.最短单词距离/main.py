#!/usr/bin/env python
from typing import List

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        pa = pb = float('-inf')
        ans = float('inf')
        for i, word in enumerate(wordsDict):
            if word == word1:
                pa = i
                ans = min(ans, pa - pb)
            elif word == word2:
                pb = i
                ans = min(ans, pb - pa)
        return ans