#!/usr/bin/env python
from typing import List

import math
from collections import defaultdict
class Solution:
    def getFactors(self, num: int) -> set:
        '''
        给定num，求出除了1和num本身以外的所有因数
        '''
        factors = set()
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                factors.add(i)
                factors.add(num // i)
        return factors

    def simplifiedFractions(self, n: int) -> List[str]:
        num2factors = defaultdict(set)
        ans = []
        for num in range(2, n+1):
            num2factors[num] = self.getFactors(num)
            for cand in range(1, num):
                if not num2factors[cand].intersection(num2factors[num]) and \
                        cand not in num2factors[num]:    # 可以被收割的条件是 1.两个因数哈希集交集是空，2.分子也不是分母的因数
                    ans.append(f"{cand}/{num}")
        return ans