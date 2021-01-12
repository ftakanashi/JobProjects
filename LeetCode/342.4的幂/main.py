#!/usr/bin/env python

class Solution1:
    def isPowerOfFour(self, n: int) -> bool:
        if n < 0: return False
        i = 0
        found_one = False
        while n > 0:
            v = n & 1
            i += 1
            if v == 1:
                if found_one: return False    # 一旦发现数目中有两个以上的1，直接返回false
                found_one = True
            n = n >> 1
        return i & 1 == 1