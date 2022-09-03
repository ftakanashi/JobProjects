#!/usr/bin/env python
from typing import List

class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        is_even = [num & 1 == 0 for num in nums]    # 统计所有位置的奇偶性
        ans = []
        s = sum([num for num in nums if num & 1 == 0])    # 初始时所有偶数的和，后续所有偶数的和也实时维护在这个变量上
        for val, ind in queries:
            val_even = (val & 1 == 0)    # 当前值的奇偶性
            if is_even[ind]:
                if val_even:
                    s += val    # 若该位置本来就是偶数，新值也是偶数，则直接加进s，同时奇偶性不变
                else:
                    s -= nums[ind]    # 奇偶性变化
                    is_even[ind] = False
            elif not val_even:    # 当该位置本来是计数，而当前值也是奇数
                s += (val + nums[ind])    # 别忘了新增 nums[ind]，以及奇偶性也变了
                is_even[ind] = True
            nums[ind] += val
            ans.append(s)

        return ans