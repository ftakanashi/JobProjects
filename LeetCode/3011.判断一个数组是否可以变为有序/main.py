#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def canSortArray(self, nums: List[int]) -> bool:
        prev_flag = prev_group_max = group_max = -1
        for num in nums:
            flag = num.bit_count()
            if flag == prev_flag:
                group_max = max(group_max, num)
            else:
                prev_flag = flag
                prev_group_max = group_max
                group_max = num
            if num < prev_group_max:
                return False

        return True