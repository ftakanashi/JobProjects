#!/usr/bin/env python

from collections import Counter
class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = Counter(s)
        flag = True
        for num in counter:
            if counter[num] & 1 == 1:
                if flag:
                    flag = False
                else:
                    return False
        return True