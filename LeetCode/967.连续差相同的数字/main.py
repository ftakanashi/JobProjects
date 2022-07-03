#!/usr/bin/env python
from typing import List

class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        digits = []
        ans = []

        def dfs():
            if len(digits) == n:
                ans.append(int("".join(f"{d}" for d in digits)))
                return

            if len(digits) == 0:
                for d in range(1, 10):
                    digits.append(d)
                    dfs()
                    digits.pop()
            else:
                tail = digits[-1]
                if tail - k >= 0:
                    digits.append(tail - k)
                    dfs()
                    digits.pop()
                if tail + k < 10 and k > 0:
                    digits.append(tail + k)
                    dfs()
                    digits.pop()

        dfs()
        return ans