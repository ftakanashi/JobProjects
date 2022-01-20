#!/usr/bin/env python

class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dp = [1 for _ in range(5)]
        MOD = 10 ** 9 + 7
        for _ in range(n-1):
            a_cnt = (dp[1] + dp[2] + dp[4]) % MOD
            e_cnt = (dp[0] + dp[2]) % MOD
            i_cnt = (dp[1] + dp[3]) %MOD
            o_cnt = dp[2] % MOD
            u_cnt = (dp[2] + dp[3]) % MOD
            dp = [a_cnt, e_cnt, i_cnt, o_cnt, u_cnt]
        return sum(dp) % MOD