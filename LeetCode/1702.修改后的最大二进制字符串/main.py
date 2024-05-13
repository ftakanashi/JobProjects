#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def maximumBinaryString(self, binary: str) -> str:
        i = 0
        while i < len(binary) and binary[i] == '1':
            i += 1
        pre = binary[:i]
        binary = binary[i:]
        if binary.count('0') == 0:
            ans = binary
        else:
            ans = (binary.count('0') - 1) * '1' + '0' + binary.count('1') * '1'
        return pre + ans
