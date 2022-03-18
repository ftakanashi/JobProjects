#!/usr/bin/env python
from typing import List

from collections import Counter
MOD = 10 ** 9 + 7
class Solution:
    def numberOfGoodSubsets(self, nums: List[int]) -> int:
        # 预处理：数字 -> 质因子集合
        n2f = {}
        for num in [1,2,3,5,7,11,13,17,19,23,29]:
            n2f[num] = {num}
        n2f.update({
            6: {2, 3}, 10: {2, 5}, 14: {2, 7},
            15: {3, 5}, 21: {3, 7}, 22: {2, 11},
            26: {2, 13}, 30: {2, 3, 5}
        })

        # 预处理：去掉所有不可能出现在子集中的数字并计数且排序
        counter = Counter([num for num in nums if num in n2f])
        nums = list(counter.keys())
        nums.sort()

        def dfs(pos, used_factors):
            if pos == len(nums): return 1 if len(used_factors) > 0 else 0    # 若扫描到末尾但used_factors是空，意义是选择了空子集，按题意不算在结果内
            num = nums[pos]
            res = 0
            if not n2f[num].intersection(used_factors):    # 数字num可以被选入子集
                res += counter[num] * dfs(pos + 1, used_factors.union(n2f[num]))
            res += dfs(pos + 1, used_factors)
            return res % MOD

        if counter[1] > 0:    # 特殊情况： 1的处理
            base = 1
            for _ in range(counter[1]):
                base = (base * 2) % MOD
            res = base * dfs(1, set())
        else:
            res = dfs(0, set())
        return res % MOD