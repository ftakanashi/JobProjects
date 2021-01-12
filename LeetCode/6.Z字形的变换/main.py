#!/usr/bin/env python
from typing import List

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) <= numRows:
            return s
        i = 0
        res = ''
        while i < len(s):
            res += s[i]
            i += (2*numRows - 2)

        n = 1
        while n < numRows - 1:
            res += s[n]
            i = 0
            while True:
                i += (2*numRows - 2)
                if i - n < len(s):
                    res += s[i - n]
                if i + n < len(s):
                    res += s[i + n]
                if i >= len(s): break
            n += 1

        i = numRows - 1
        while i < len(s):
            res += s[i]
            i += (2*numRows - 2)

        return res

