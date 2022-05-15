#!/usr/bin/env python
from typing import List


class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        ans = i = j = 0    # 滑窗模板：进行两个指针以及答案的初始化
        n = len(nums)
        s = 1    # 滑窗模板：进行窗口合法指标的初始化
        while j < n:    # 滑窗模板：以右指针不越界为条件进行滑动
            s *= nums[j]    # 滑窗模板：第一步先更新窗口合法指标
            while i < j and s >= k:     # 若不合法了，收缩左指针
                s //= nums[i]
                i += 1

            # 滑窗模板：直接收割结果，不过这题这里需要注意分类讨论
            if j > i:
                ans += (j - i + 1)
            elif nums[j] < k:    # 隐含条件 i == j
                ans += 1

            j += 1    # 滑窗模板：别忘了移动右指针

        return ans