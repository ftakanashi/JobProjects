#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # 其实前两个分支也还可以进一步合并
        if k <= numOnes:
            return k
        elif k <= numOnes + numZeros:
            return numOnes
        else:
            return numOnes - (k - numOnes - numZeros)