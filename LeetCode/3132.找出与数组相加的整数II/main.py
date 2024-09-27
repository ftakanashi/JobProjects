#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minimumAddedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        for pivot in range(2, -1, -1):
            diff = nums2[0] - nums1[pivot]
            i, j = pivot + 1, 1
            while i < len(nums1) and j < len(nums2):
                if nums2[j] - nums1[i] == diff:
                    j += 1
                i += 1
            if j == len(nums2):
                return diff

        return -1    # 题目保证有解，所以不会走到这里