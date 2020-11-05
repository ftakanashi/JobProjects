#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        # if len(A) < 3: return False    # 题目明明说A.length >= 3，不知道为啥case里还有不符合要求的…

        i, j = 0, len(A) - 1
        prev_i, prev_j = float('-inf'), float('-inf')

        while i < len(A) and prev_i < A[i]:
            prev_i = A[i]
            i += 1
        i -= 1

        while j >= 0 and prev_j < A[j]:
            prev_j = A[j]
            j -= 1
        j += 1

        if i == 0 or j == len(A) - 1: return False

        return i == j