#!/usr/bin/nev python
from typing import List

class Solution1:
    def maxSubArray(self, nums: List[int]) -> int:
        n = len(nums)

        prev_s = max_s = nums[0]
        for i in range(1, n):
            s = max(prev_s + nums[i], nums[i])
            if s > max_s:
                max_s = s
            prev_s = s
        return max_s

        # 无状态压缩版本
        # dp = [0 for _ in range(n)]
        # dp[0] = nums[0]
        # for i in range(1, n):
        #     dp[i] = max(dp[i-1]+nums[i], nums[i])
        #
        # return max(dp)

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        presum = [0,]
        for num in nums:
            presum.append(presum[-1] + num)

        ans = float('-inf')
        min_v = float('inf')
        for s in presum:
            ans = max(ans, s - min_v)
            if s < min_v: min_v = s
        return ans

        # 使用堆的方案
        # heap = []
        # for s in presum:
        #     if heap:
        #         ans = max(ans, s - heap[0])
        #     heapq.heappush(heap, s)
        # return ans