#!/usr/bin/env python
class Solution:
    def superEggDrop(self, K: int, N: int) -> int:

        ### 这部分注释是用经典DP二维矩阵做的情况
        # F = float('inf')
        # dp = [[F for _ in range(N+1)] for _ in range(K+1)]
        # for i in range(K+1):
        #     dp[i][0] = 0
        # for j in range(N+1):
        #     dp[1][j] = j

        # for i in range(2, K+1):
        #     for j in range(1, N+1):
        #
        #         ### 这部分注释是无二分查找优化的情况
        #         # v = F
        #         # for x in range(1, j+1):
        #         #     v = min(
        #         #         v,
        #         #         max(dp[i-1][x-1], dp[i][j-x]) + 1
        #         #     )

        #         l, r = 1, j
        #         while l <= r:
        #             mid = (l + r) // 2
        #             if dp[i-1][mid-1] >= dp[i][j-mid]:
        #                 r = mid - 1
        #             else:
        #                 l = mid + 1

        #         dp[i][j] = min(dp[i-1][l-1], dp[i][j-r]) + 1

        # return dp[-1][-1]

        memo = {}
        def dp(k, n):
            if (k, n) not in memo:
                if n == 0:
                    memo[k, n] = 0
                elif k == 1:
                    memo[k, n] = n
                else:
                    l, r = 1, n
                    while l + 1 < r:
                        mid = (l + r) // 2
                        t1, t2 = dp(k-1, mid-1), dp(k, n-mid)
                        if t1 < t2: l = mid
                        elif t1 > t2: r = mid
                        else: l = r = mid

                    memo[k, n] = min( max(dp(k-1, x-1), dp(k, n-x)) for x in (l, r) ) + 1

            return memo[k, n]

        return dp(K, N)