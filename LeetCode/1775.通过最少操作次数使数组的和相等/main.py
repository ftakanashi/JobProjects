#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

import math
from collections import Counter

class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        l1, l2 = len(nums1), len(nums2)
        if l1 * 6 < l2 or l2 * 6 < l1: return -1

        s1 = s2 = 0
        cnt1 = Counter()
        cnt2 = Counter()
        for num in nums1:
            s1 += num
            cnt1[num] += 1
        for num in nums2:
            s2 += num
            cnt2[num] += 1

        if s1 > s2:
            large_sum, large_count = s1, cnt1
            small_sum, small_count = s2, cnt2
        else:
            large_sum, large_count = s2, cnt2
            small_sum, small_count = s1, cnt1

        # 至此，也只是计算出两个数组各自的总和，计数，并根据大小重构变量，方便下面的操作

        # 统计贡献值
        contrib = Counter()
        for i in range(1, 7):
            contrib[i-1] += large_count[i]
            contrib[6-i] += small_count[i]

        ans = 0
        diff = large_sum - small_sum
        for num in sorted(contrib, reverse=True):
            if diff > num * contrib[num]:
                # 若某类贡献值全部用上也弥补不了diff的情况
                diff -= num * contrib[num]
                ans += contrib[num]
            else:
                ans += math.ceil(diff / num)
                break
        return ans