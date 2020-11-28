#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution1:
    def maximumGap(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return 0

        # 基数排序开始
        n = len(str(max(nums)))
        for k in range(n):
            buckets = [[] for _ in range(10)]
            for n in nums:
                radix = int((n / (10 ** k)) % 10)
                buckets[radix].append(n)

            nums = []    # 记得基数排序要把上一个循环中完成排序的列表给抽取出来，给下一个循环用
            for b in buckets:
                nums.extend(b)
        # 基数排序结束
        # 以上基数排序操作可以整体用一个nums.sort()来代替

        max_gap = 0
        for i in range(len(nums) - 1):
            max_gap = max(max_gap, nums[i+1]-nums[i])
        return max_gap