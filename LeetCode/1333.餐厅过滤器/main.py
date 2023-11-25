#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def filterRestaurants(self, restaurants: List[List[int]], veganFriendly: int, maxPrice: int, maxDistance: int) -> List[int]:
        filtered = [r for r in restaurants if r[3] <= maxPrice and r[4] <= maxDistance and not (veganFriendly and not r[2])]
        filtered.sort(key=lambda r: (-r[1], -r[0]))
        return [r[0] for r in filtered]