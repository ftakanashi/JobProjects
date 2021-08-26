#!/usr/bin/env python
class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7
        # dp = [
        #     [[0,0,0], [0,0,0]] for _ in range(n)
        #     ]
        # dp[0] = [[1, 1, 0], [1, 0, 0]]
        # for i in range(1, n):
        #     mat = dp[i]
        #     prev = dp[i-1]
        #     mat[0][0] = (prev[0][0] + prev[0][1] + prev[0][2]) % MOD
        #     mat[0][1] = prev[0][0] % MOD
        #     mat[0][2] = prev[0][1] % MOD
        #     mat[1][0] = sum([sum(row) for row in prev]) % MOD
        #     mat[1][1] = prev[1][0] % MOD
        #     mat[1][2] = prev[1][1] % MOD
        # return sum([sum(row) for row in dp[-1]]) % MOD
        mat = [[1, 1, 0], [1, 0, 0]]
        for _ in range(1, n):
            new = [[0,0,0], [0,0,0]]
            new[0][0] = sum(mat[0]) % MOD
            new[0][1], new[0][2] = mat[0][0] % MOD, mat[0][1] % MOD
            new[1][0] = sum((sum(row) for row in mat)) % MOD
            new[1][1], new[1][2] = mat[1][0] % MOD, mat[1][1] % MOD
            mat = new

        res = 0
        for row in mat:
            for item in row:
                res = (res + item) % MOD
        return res