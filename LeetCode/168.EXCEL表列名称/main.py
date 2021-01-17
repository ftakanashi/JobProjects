#!/usr/bin/env python

class Solution:
    def convertToTitle(self, n: int) -> str:
        res = ''
        while n > 0:
            remind = n % 26
            if remind == 0:
                res = chr(64 + 26) + res
                n = n // 26 - 1
            else:
                res = chr(64 + remind) + res
                n = n // 26

        return res