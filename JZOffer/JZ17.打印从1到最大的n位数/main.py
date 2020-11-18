#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def printNumbers(self, n: int) -> List[int]:
        digits = ['1', ]
        res = []
        while len(digits) <= n:
            res.append(int(''.join(digits)))
            self.addOne(digits, len(digits) - 1)
        return res

    def addOne(self, digits, i):
        if i < 0:
            digits.insert(0, '1')
        elif digits[i] != '9':
            digits[i] = chr(ord(digits[i]) + 1)
        else:
            digits[i] = '0'
            self.addOne(digits, i - 1)

    '''
    # 递推版
    def addOne(self, digits):
    i = len(digits) - 1
    while True:
        if i < 0:
            digits.insert(0, '1')
            break
        if digits[i] == '9':
            digits[i] = '0'
            i -= 1
        else:
            digits[i] = chr(ord(digits[i]) + 1)
            break
    
    '''