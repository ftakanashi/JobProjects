#!/usr/bin/env python
class Solution:
    def isStrobogrammatic(self, num: str) -> bool:
        digit_map = {
            "6": "9",
            "9": "6",
            "0": "0",
            "1": "1",
            "8": "8"
        }
        i, j = 0, len(num) - 1
        while i <= j:
            if num[i] in digit_map and digit_map[num[i]] == num[j]:
                i += 1
                j -= 1
            else:
                break
        return i > j

