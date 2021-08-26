#!/usr/bin/env python
from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort(reverse=True)
        i, j = 0, len(people) - 1
        cnt = 0
        while i < j:
            cnt += 1
            if people[i] + people[j] <= limit:
                j -= 1
            i += 1

        if i == j:
            cnt += 1

        return cnt