#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

from collections import Counter, deque
class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        ans = [None for _ in range(len(barcodes))]

        # 为了后面方便，构造填充下标的顺序序列
        indices = list(range(0, len(barcodes), 2)) + list(range(1, len(barcodes), 2))
        indices = deque(indices)

        for code in sorted(counter, key=lambda x: counter[x], reverse=True):
            cnt = counter[code]
            for _ in range(cnt):
                i = indices.popleft()    # 由于counter的各个计数值的和一定等于indices的初始长度，所以这里都不用校验，当counter遍历到最后一个数字，indices也肯定正好用完
                ans[i] = code

        return ans