#!/usr/bin/env python
class Solution:
    def removePalindromeSub(self, s: str) -> int:
        return 1 if s == "".join(reversed(s)) else 2