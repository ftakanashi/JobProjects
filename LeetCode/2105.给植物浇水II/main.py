#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def minimumRefill(self, plants: List[int], capacityA: int, capacityB: int) -> int:
        ans = 0
        i, j = 0, len(plants) - 1
        a, b = capacityA, capacityB
        while i <= j:

            # 到达同一个植物
            if i == j:
                ans += 1 if max((a, b)) < plants[i] else 0
                # 由于只需要返回灌水次数，因此这次是谁浇水并不重要，只要看他有没有灌水即可
            else:
                # Alice
                if a >= plants[i]:
                    a -= plants[i]
                else:
                    a = capacityA - plants[i]
                    ans += 1
                # Bob
                if b >= plants[j]:
                    b -= plants[j]
                else:
                    b = capacityB - plants[j]
                    ans += 1

            i += 1
            j -= 1

        return ans