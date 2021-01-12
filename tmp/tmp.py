#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

def convert(s: str, numRows: int) -> str:
    i = 0
    res = ''
    while i < len(s):
        res += s[i]
        i += (2*numRows - 2)

    n = 1
    while n < numRows - 1:
        i = n
        res += s[i]
        while True:
            i += (2*numRows - 2)
            if i >= len(s): break
            if i - n < len(s):
                res += s[i - n]
            if i + n < len(s):
                res += s[i + n]
        n += 1

    i = numRows - 1
    while i < len(s):
        res += s[i]
        i += (2*numRows - 2)

    return res

if __name__ == '__main__':
    print(convert('PAYPALISHIRING', 3))