#!/usr/bin/env python
from typing import List

class Solution:
    def check(self, word, pattern):
        m, r = {}, {}
        for i in range(len(word)):
            if word[i] not in m:
                if pattern[i] in r: return False
                m[word[i]] = pattern[i]
                r[pattern[i]] = word[i]
            else:
                if m[word[i]] != pattern[i]: return False
        return True

    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        return [word for word in words if self.check(word, pattern)]