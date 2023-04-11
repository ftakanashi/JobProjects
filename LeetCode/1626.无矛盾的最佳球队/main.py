#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        members = [(s, a) for s, a in zip(scores, ages)]
        members.sort()

        dp = [m[0] for m in members]    # DP数组初始值为各个队员的score
        for i, (score, age) in enumerate(members):
            for j in range(i):
                if members[j][1] <= age:
                    dp[i] = max(dp[i], dp[j] + score)

        return max(dp)