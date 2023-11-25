#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n, MOD = len(arr), 10 ** 9 + 7

        arr.sort()
        arr2pos = {num: i for i, num in enumerate(arr)}
        dp = [1 for _ in range(n)]

        for i in range(1, n):
            seen = set()
            for j in range(i):
                if arr[j] in seen: continue
                if arr[i] % arr[j] == 0:
                    rest = arr[i] // arr[j]
                    if rest not in arr2pos: continue
                    seen.add(rest)
                    p = arr2pos[rest]
                    vol = (dp[p] * dp[j]) % MOD
                    if rest != arr[j]:
                        vol = (vol * 2) % MOD
                    dp[i] = (dp[i] + vol) % MOD

        ans = 0
        for num in dp:
            ans = (ans + num) % MOD
        return ans