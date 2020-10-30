#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution1:
    def minArray(self, numbers: List[int]) -> int:

        last = float('-inf')
        i = 0
        while i < len(numbers):
            if numbers[i] < last:
                return numbers[i]
            last = numbers[i]
            i += 1

        return numbers[0]


class Solution2:
    def minArray(self, numbers: List[int]) -> int:

        if len(numbers) == 1: return numbers[0]

        left, right = 0, len(numbers) - 1

        while left < right:
            mid = (left + right) // 2
            if numbers[mid] > numbers[right]:
                left = mid + 1
            elif numbers[mid] < numbers[right]:
                right = mid
            else:
                right -= 1

        return numbers[left]