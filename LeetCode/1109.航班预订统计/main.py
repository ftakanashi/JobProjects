#!/usr/bin/env python
from typing import List

class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        diff = [0 for _ in range(n+2)]
        for first, last, seats in bookings:
            diff[first] += seats
            diff[last+1] -= seats
        ans = []
        s = 0
        for i in range(1, n+1):
            s += diff[i]
            ans.append(s)
        return ans