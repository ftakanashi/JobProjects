#!/usr/bin/env python
from typing import List

from collections import defaultdict
class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.map = defaultdict(list)
        for i, word in enumerate(wordsDict):
            self.map[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        p1 = p2 = 0
        ans = float('inf')
        indices1, indices2 = self.map[word1], self.map[word2]
        m, n = len(indices1), len(indices2)
        while p1 < m and p2 < n:
            if indices1[p1] < indices2[p2]:
                ans = min(ans, indices2[p2] - indices1[p1])
                p1 += 1
            else:
                ans = min(ans, indices1[p1] - indices2[p2])
                p2 += 1

        return ans

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)