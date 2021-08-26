#!/usr/bin/env python
import re
class Solution:
    def checkRecord(self, s: str) -> bool:
        n = len(s)
        if n == 1: return True
        if n == 2: return s != 'AA'
        if s[:2] == 'LL':
            l_cnt = 2
        elif s[1] == 'L':
            l_cnt = 1
        else:
            l_cnt = 0
        a_cnt = s[:2].count('A')
        for i in range(2, n):
            ch = s[i]
            if ch == 'P':
                l_cnt = 0
            elif ch == 'A':
                l_cnt = 0
                a_cnt += 1
            elif ch == 'L':
                l_cnt += 1

            if a_cnt >= 2 or l_cnt >= 3:
                return False

        return True