#!/usr/bin/env python

from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        BIT = 30
        res = 0
        for bit in range(BIT-1, -1, -1):    # 确定一个位
            cnt = 0
            for n in nums:    # 统计各个数字在这个位上是1的计数
                cnt += (n>>bit) & 1
            res += cnt * (len(nums) - cnt)    # 1的计数乘以0的计数是这个位贡献的汉明距离

        return res