#!/usr/bin/env python

from typing import List

class Solution1:
    def check(self, jobs, k, limit):
        times = [0 for _ in range(k)]
        def dfs(start):
            if start == len(jobs): return True
            job = jobs[start]
            for i in range(k):
                if times[i] + job > limit: continue
                times[i] += job
                if dfs(start + 1): return True
                times[i] -= job

                if times[i] == 0: break    # 重要！因为工人是无序的，所以天然的，不允许times中非零值出现在零值的右边。

            return False

        return dfs(0)

    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        if n <= k: return max(jobs)
        l, r = max(jobs), sum(jobs)
        jobs.sort(reverse=True)    # 加这条可以进一步优化
        while l <= r:
            mid = (l + r) // 2
            if self.check(jobs, k, mid):
                r = mid - 1
            else:
                l = mid + 1
        return l

class Solution2:
    def minimumTimeRequired(self, jobs: List[int], k: int) -> int:
        n = len(jobs)
        if n <= k: return max(jobs)
        dp = [[0 for _ in range(2**n)] for _ in range(k)]

        for j in range(2**n):
            num = j
            res = bit = 0
            while num > 0:
                if num & 1 == 1: res += jobs[bit]
                bit += 1
                num = num >> 1
            dp[0][j] = res

        for i in range(1, k):
            for j in range(1, 2**n):
                x, min_v = j, dp[i-1][j]
                while x > 0:
                    y = j - x
                    min_v = min(min_v, max(dp[i-1][y], dp[0][x]))
                    x = (x - 1) & j

                dp[i][j] = min_v
        # print(dp)
        return dp[k-1][2**n-1]