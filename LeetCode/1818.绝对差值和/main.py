#!/usr/bin/env python
from typing import List

import bisect
class Solution:
    def minAbsoluteSumDiff(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        ans = 0
        contrib = float('-inf')
        sorted_nums1 = list(sorted(nums1))
        for i, num in enumerate(nums2):
            # 计算原生的 nums1[i]与nums2[i] 间的差，并统计到ans中
            diff = abs(num - nums1[i])
            ans += diff

            # 计算把nums1[i]替换掉后能提供的最大贡献值
            j = bisect.bisect_left(sorted_nums1, num)
            contrib1 = diff - abs(num - sorted_nums1[j]) if j < n else 0
            contrib2 = diff - abs(num - sorted_nums1[j-1]) if j > 0 else 0
            contrib = max(contrib, contrib1, contrib2)

        ans -= contrib
        return ans % (10**9 + 7)    # 最后别忘了题目要求要取余