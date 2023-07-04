#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def miceAndCheese(self, reward1: List[int], reward2: List[int], k: int) -> int:
        n = len(reward1)

        # 因为需要将奶酪收益和奶酪对应起来，因此需要将下标i作为标识也放到数组中
        benifits = [(reward1[i] - reward2[i], i) for i in range(n)]
        benifits.sort(reverse=True)

        ans = 0
        for i in range(k):
            ans += reward1[benifits[i][1]]

        for i in range(k, n):
            ans += reward2[benifits[i][1]]

        return ans