#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

def generate_pnext(s: str) -> List[int]:
    i, k, m = 0, -1, len(s)
    pnext = [-1 for _ in range(m)]
    while i < m-1:
        if k == -1 or s[i] == s[k]:
            pnext[i + 1] = k + 1
            i += 1
            k += 1
        else:
            k = pnext[k]

    return pnext

def kmp(t, p):
    pnext = generate_pnext(p)
    j, i = 0, 0
    n, m = len(t), len(p)
    while j < n and i < m:
        if i == -1 or t[j] == p[i]:
            i += 1
            j += 1
        else:
            i = pnext[i]
    if i == m: return j - i
    return -1

print(kmp('abababbabaa','abba'))