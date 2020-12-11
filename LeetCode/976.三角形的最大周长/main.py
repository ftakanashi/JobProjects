#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        A.sort()
        i = len(A) - 3
        while i >= 0:
            if A[i] + A[i+1] > A[i+2]:
                return A[i] + A[i+1] + A[i+2]
            i -= 1

        return 0