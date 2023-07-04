#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def addNegabinary(self, arr1: List[int], arr2: List[int]) -> List[int]:
        if len(arr1) < len(arr2):
            arr1, arr2 = arr2, arr1
        arr1.reverse()
        arr2.reverse()
        i = j = 0
        ans = []
        carry = 0
        while i < len(arr1) or j < len(arr2) or carry != 0:
            x = carry
            if i < len(arr1): x += arr1[i]
            if j < len(arr2): x += arr2[j]
            # 以 x 表示某个特定的位置初次加出来的和是多少，根据下面的规则具体决定进位和最终值

            if x >= 2:
                ans.append(x - 2)
                carry = -1
            elif x >= 0:
                ans.append(x)
                carry = 0
            else:
                ans.append(1)
                carry = 1

            i += 1
            j += 1

        # 处理可能的前导零
        while len(ans) > 1 and ans[-1] == 0:
            ans.pop()

        ans.reverse()    # 最后别忘了reverse一下，因为是倒着加上去的
        return ans