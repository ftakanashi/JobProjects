#!/usr/bin/env python
from typing import List

from collections import defaultdict
class Solution:
    def myHash(self, string: str):
        n = len(string)
        if n == 1: return 0
        ans = []
        for i in range(1, n):
            diff = ord(string[i]) - ord(string[i - 1])
            ans.append(diff if diff >= 0 else 26+diff)
        return tuple(ans)

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        mapping = defaultdict(list)
        for s in strings:
            h = self.myHash(s)
            mapping[h].append(s)

        return list(mapping.values())