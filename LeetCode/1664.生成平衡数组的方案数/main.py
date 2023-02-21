#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        pre_odd = pre_even = suf_odd = suf_even = 0
        ans = 0

        for i, num in enumerate(nums):
            if i & 1 == 0:
                suf_odd += num
            else:
                suf_even += num

        # 遍历每个位置 i ，尝试删除下标为 i 的元素后是判断否得到平衡数组
        for i, num in enumerate(nums):
            # 判断前，先从suf值中减去 num
            if i & 1 == 0:
                suf_odd -= num
            else:
                suf_even -= num

            # 判断
            if pre_odd + suf_even == pre_even + suf_odd:
                ans += 1

            # 判断完之后再向 pre值中增加 num
            if i & 1 == 0:
                pre_odd += num
            else:
                pre_even += num

        return ans