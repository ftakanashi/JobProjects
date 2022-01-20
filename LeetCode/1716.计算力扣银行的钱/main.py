#!/usr/bin/env python

class Solution:
    def totalMoney(self, n: int) -> int:
        weeks = n // 7    # 在第n天，到上一周的周日为止的总周数
        days = n % 7    # 在第n天，本周一到今天的天数

        s, e = 28, 28 + (weeks - 1) * 7
        ans = (s + e) * weeks // 2    # 等差数列求和求出之前所有周总数
        for d in range(days):
            ans += (weeks + 1 + d)    # 加上本周的数
        return ans