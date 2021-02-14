#!/usr/bin/env python
from typing import List

class Solution:
    def check_base_n(self, s:str) -> bool:
        if len(s) == 0: return False
        if s[0] in '+-': s = s[1:]
        if len(s) == 0 or '+' in s or '-' in s: return False
        if '.' in s:
            split_nums = s.split('.')
            if len(split_nums) != 2: return False
            a, b = split_nums
            if a == '' and b == '': return False
        return True

    def check_pow_n(self, s: str) -> bool:
        if len(s) == 0 or '.' in s: return False
        if s[0] in '+-': s = s[1:]
        if len(s) == 0 or '+' in s or '-' in s: return False
        return True

    def isNumber(self, s: str) -> bool:
        valid_chs = '1234567890+-eE.'
        s = s.strip()
        for ch in s:
            if ch not in valid_chs: return False

        s = s.lower()
        if 'e' in s:
            split_nums = s.split('e')
            if len(split_nums) != 2: return False
            base_n, pow_n = split_nums
            return self.check_base_n(base_n) and self.check_pow_n(pow_n)
        else:
            return self.check_base_n(s)