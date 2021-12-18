#!/usr/bin/env python
from typing import List

from collections import Counter
class Solution:
    def shortestCompletingWord(self, licensePlate: str, words: List[str]) -> str:
        lic_counter = Counter()
        for ch in licensePlate.lower():
            if ord('a') <= ord(ch) <= ord('z'):
                lic_counter[ch] += 1

        min_len = float('inf')
        ans = None
        for word in words:
            word_len = len(word)
            if word_len >= min_len: continue
            word_counter = Counter(word)
            flag = True
            for key in lic_counter:
                if lic_counter[key] > word_counter[key]:
                    flag = False
                    break

            if flag:
                min_len = word_len
                ans = word
        return ans