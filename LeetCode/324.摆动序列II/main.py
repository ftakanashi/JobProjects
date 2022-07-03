#!/usr/bin/env python
from typing import List

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        n = len(nums)
        sorted_nums = list(sorted(nums))

        i = (n + 1) // 2 - 1
        j = n - 1
        pos = 0
        while pos < n:
            nums[pos] = sorted_nums[i]
            if pos + 1 < n:
                nums[pos + 1] = sorted_nums[j]
            pos += 2
            i -= 1
            j -= 1