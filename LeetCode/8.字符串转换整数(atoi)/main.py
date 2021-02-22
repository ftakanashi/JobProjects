#!/usr/bin/env python

class Solution:
    def myAtoi(self, s: str) -> int:
        table = [
            [0, 1, 2, 3],
            [3, 3, 2, 3],
            [3, 3, 2, 3],
            [3, 3, 3, 3]
        ]
        MAX = 2**31 - 1

        def char_type(ch):
            if ch == ' ': return 0
            if ch in '+-': return 1
            if ch in '1234567890': return 2
            return 3

        i, res, state, minus = 0, 0, 0, False
        for ch in s:
            state = table[state][char_type(ch)]
            if state == 1: minus = ch == '-'
            if state == 2:
                digit = ord(ch) - ord('0')
                if res > MAX // 10 or (res == MAX // 10 and digit >= 8):
                    res = MAX + 1 if minus else MAX
                    break
                res = res * 10 + digit
            if state == 3: break

        return -res if minus else res