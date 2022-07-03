#!/usr/bin/env python
from typing import List

import bisect

from collections import defaultdict

class Solution:
    def findClosest(self, words: List[str], word1: str, word2: str) -> int:
        word2i = defaultdict(list)
        for i, word in enumerate(words):
            word2i[word].append(i)

        word1_indices = word2i[word1]
        word2_indices = word2i[word2]
        if len(word1_indices) > len(word2_indices):
            tmp = word2_indices
            word2_indices = word1_indices
            word1_indices = tmp

        ans = float('inf')
        for i in word1_indices:
            pos = bisect.bisect(word2_indices, i)
            if pos < len(word2_indices):
                ans = min(ans, abs(word2_indices[pos] - i))
            if pos > 0:
                ans = min(ans, abs(word2_indices[pos - 1] - i))
        return ans