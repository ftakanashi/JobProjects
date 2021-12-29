#!/usr/bin/env python
from typing import List

import bisect
from collections import Counter
class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        ages.sort()    # 别被例子蒙骗了，ages本身乱序，需要排序
        counter = Counter(ages)
        ans = 0
        for age in counter:    # 先统计所有"年龄内"的请求数量
            if age > 14 and counter[age] > 1:
                ans += (counter[age] * (counter[age] - 1))

        diff = 0    # 额外变量用于记录可能的上一轮的请求数
        for x in range(len(ages)):
            if ages[x] <= 14: continue
            if x > 0 and ages[x] == ages[x-1]:
                ans += diff    # 当重复年龄出现，直接适用该年龄第一次出现时得到的结果
                continue
            y = bisect.bisect(ages, ages[x] // 2 + 7)    # 由于题目要求的下界不能取到等于，因此使用bisect_right
            diff = x - y
            ans += diff
        return ans