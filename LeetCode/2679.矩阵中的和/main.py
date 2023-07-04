#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def matrixSum(self, nums: List[List[int]]) -> int:
        m, n = len(nums), len(nums[0])
        ans = 0

        # 给每行排序
        for row in nums:
            row.sort(reverse=True)

        # 计算第 j 大数的总和
        for j in range(n):
            ans += max(row[j] for row in nums)

        return ans