#!/usr/bin/env python
from typing import List

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)
        if n < 10: return []
        ans = set()
        seen = set()
        i, j = 0, 9
        while j < n:
            sub = s[i:j+1]
            if sub in seen and sub not in ans:
                ans.add(sub)
            seen.add(sub)
            i += 1
            j += 1
        return list(ans)