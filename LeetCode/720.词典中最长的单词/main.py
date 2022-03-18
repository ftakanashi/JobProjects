#!/usr/bin/env python
from typing import List

class Solution:
    def longestWord(self, words: List[str]) -> str:
        seen = set(words)
        ans = ""
        for word in sorted(words, reverse=True, key=lambda x:len(x)):
            if len(word) < len(ans): break
            flag = True
            for i in range(1, len(word)+1):
                prefix = word[:i]
                if prefix not in seen:
                    flag = False
                    break
            if flag:
                if len(word) > len(ans) or (len(word) == len(ans) and word < ans):
                    ans = word
        return ans