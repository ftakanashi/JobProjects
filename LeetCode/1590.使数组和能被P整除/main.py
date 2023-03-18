#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List


class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        x = sum(nums) % p    # 确定x值
        if x == 0: return 0

        presum = 0
        mod2pos = {0: -1}
        ans = float('inf')
        # 开始遍历
        for i, num in enumerate(nums):
            # 维护前缀和
            presum += num

            # 这里还有个小问题，就是当presum < x的时候，presum - x是负数
            # 此时也就意味着即便把当前位置整个左边的子数组都去掉，也不够弥补总和除出来的余数，因此其实可以不考虑
            # 不过实践也发现，Python对于负数取余是适配这题的
            if presum - x >= 0:
                mod = (presum - x) % p
                if mod in mod2pos:
                    ans = min(ans, i - mod2pos[mod])

            # 更新哈希表
            mod2pos[presum % p] = i

        # 此时如果ans == len(nums)，也就意味着要把整个数组移除，剩下数组的和为0，才能被p整除，根据题意，此时应该返回-1
        return ans if ans < len(nums) else -1