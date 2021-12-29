#!/usr/bin/env python
from typing import List
from bisect import bisect_left

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        ans = 0
        for house in houses:
            pos = bisect_left(heaters, house)    # 先二分查找heaters中house的位置，得到pos为房子后面最近的heater位置
            prev = pos - 1    # 减去1得到房子前面最近的heater位置
            min_radius = min(    # 为满足该房子供暖且半径尽可能小，选取两者距离中较小值。别忘了考虑越界的情况。
                (house - heaters[prev]) if prev >= 0 else float('inf'),
                (heaters[pos] - house) if pos < len(heaters) else float('inf')
            )
            ans = max(ans, min_radius)    # 最大化最小值
        return ans