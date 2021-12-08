#!/usr/bin/env python
from collections import Counter
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magzine_counter = Counter(magazine)
        for ch in ransomNote:
            if magzine_counter[ch] == 0:
                return False
            magzine_counter[ch] -= 1
        return True