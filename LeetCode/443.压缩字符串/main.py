#!/usr/bin/env python
from typing import List

class Solution:
    def compress(self, chars: List[str]) -> int:
        i = j = 0
        n = len(chars)
        while j < n:

            orig_j = j
            while j < n-1 and chars[j] == chars[j+1]:
                j += 1

            chars[i] = chars[j]
            i += 1

            span = j - orig_j + 1
            if span > 1:
                for digit in str(span):
                    chars[i] = digit
                    i += 1

            j += 1
        return i