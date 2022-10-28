#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        min_right = []
        for i in range(n-1, -1, -1):
            if not min_right or nums[i] < min_right[-1]:
                min_right.append(nums[i])
            else:
                min_right.append(min_right[-1])
        min_right.reverse()

        max_left = nums[0]
        for i in range(1, n):
            if max_left <= min_right[i]:
                return i
            max_left = max(max_left, nums[i])