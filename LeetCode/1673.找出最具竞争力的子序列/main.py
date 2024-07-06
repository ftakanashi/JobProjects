#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def mostCompetitive(self, nums: List[int], k: int) -> List[int]:
        stack = []
        n = len(nums)

        for i, num in enumerate(nums):
            while stack and len(stack) + (n - i) > k and stack[-1] > num:
                stack.pop()
            stack.append(num)

        return stack[:k]