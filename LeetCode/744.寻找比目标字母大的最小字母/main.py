#!/usr/bin/env python
from typing import List

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        tord = ord(target)
        while l <= r:
            mid = (l + r) // 2
            if ord(letters[mid]) <= tord:
                l = mid + 1
            else:
                r = mid - 1
        return letters[l] if l < len(letters) else letters[0]
