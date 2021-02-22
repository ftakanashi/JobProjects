#!/usr/bin/env python
from typing import List

import collections
class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        for c in '!?\',;.':
            paragraph = paragraph.replace(c, ' ')
        counter = collections.Counter(paragraph.lower().strip().split())

        banned = set(banned)
        for w in sorted(counter, key=lambda x: counter[x], reverse=True):
            if w not in banned: return w