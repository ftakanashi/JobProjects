#!/usr/bin/env python
class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        len1, len2 = len(first), len(second)
        if abs(len1 - len2) >= 2: return False

        if len1 == len2:
            flag = False
            for i in range(len1):
                if first[i] != second[i]:
                    if flag: return False
                    flag = True

        else:
            long, short = (first, second) if len1 > len2 else (second, first)
            flag = False
            i = j = 0
            while i < len(short) and j < len(long):
                if short[i] != long[j]:
                    if flag: return False
                    flag = True
                    j += 1
                else:
                    i += 1
                    j += 1

        return True