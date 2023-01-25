#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def isIdealPermutation(self, nums: List[int]) -> bool:
        i = 0
        n = len(nums)
        while i < n:
            if nums[i] != i:
                if nums[i] == i+1 and nums[i+1] == i:
                    i += 2
                else:
                    return False
            else:
                i += 1
        return True