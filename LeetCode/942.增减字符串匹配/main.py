#!/usr/bin/env python
from typing import List
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        ans = [0, ]
        l, r = -1, 1
        for ch in s:
            if ch == "I":
                ans.append(r)
                r += 1
            else:
                ans.append(l)
                l -= 1

        diff = -min(ans)
        return [num + diff for num in ans]