#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if (n:=len(nums)) < 2:
            return n

        prevdiff = nums[1] - nums[0]
        count = 2 if prevdiff != 0 else 1
        # 特殊情况，开头就是平路。此时就不能默认至少有两个转折点。

        for i in range(2, n):
            diff = nums[i] - nums[i - 1]
            if (diff > 0 and prevdiff <= 0) or (diff < 0 and prevdiff >= 0):
                count += 1
                prevdiff = diff    # 注意这句话在if里面。说明prevdiff的定义，其实是
                # 每个单调区间第一个非平路的差值
                # 由于这个值只是拿来看符号，所以具体大小无所谓，只要知道正负即可

        return count