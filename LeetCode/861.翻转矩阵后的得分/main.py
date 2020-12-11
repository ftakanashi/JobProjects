#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def matrixScore(self, A: List[List[int]]) -> int:
        rows, cols = len(A), len(A[0])

        for r_i in range(rows):
            if A[r_i][0] == 0:
                self.flip(A, r_i, 'row')

        for j in range(1, cols):
            if sum([a[j] for a in A]) <= rows // 2:
                self.flip(A, j, 'col')

        s = 0
        for row in A:
            s += int(''.join([str(n) for n in row]), 2)
        return s

    def flip(self, A: List[List[int]], x: int, typ: str):
        '''
        翻转操作的方法
        '''
        if typ == 'row':
            tmp = [n ^ 1 for n in A[x]]
            A[x] = tmp
        elif typ == 'col':
            tmp = [n ^ 1 for n in [a[x] for a in A]]
            for r_i, a in enumerate(A):
                a[x] = tmp[r_i]