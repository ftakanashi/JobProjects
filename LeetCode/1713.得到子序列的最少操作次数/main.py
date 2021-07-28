#!/usr/bin/env python

from typing import List

import bisect
class Solution:
    def minOperations(self, target: List[int], arr: List[int]) -> int:
        target_n2i = {n: i for i, n in enumerate(target)}
        arr_prime = []
        # 构建arr'数组
        for n in arr:
            if n in target_n2i:
                arr_prime.append(target_n2i[n])

        # 二分查找 + 替换单调栈套路，详情见LC.300
        stack = []
        lis = 0
        for i in arr_prime:
            if not stack or stack[-1] < i:
                stack.append(i)
            else:
                pos = bisect.bisect_left(stack, i)
                stack[pos] = i
            lis = max(lis, len(stack))

        return len(target) - lis