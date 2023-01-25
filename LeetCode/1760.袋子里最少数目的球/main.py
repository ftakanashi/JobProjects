#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:

        ordered_num = list(sorted(nums, reverse=True))
        def check(ths):
            # 官方答案实际上就是下面这个无脑sum，反而还更快
            # return sum((num-1) // ths for num in nums) <= maxOperations

            tmp = 0
            for num in ordered_num:
                if num < ths: break
                tmp += ((num - 1) // ths)
                if tmp > maxOperations: return False
            return True

        l, r = 1, max(nums)
        while l <= r:
            mid = (l + r) // 2
            if check(mid):
                r = mid - 1
            else:
                l = mid + 1

        return l