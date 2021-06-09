#!/usr/bin/env python

class Solution1:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        x, y, z = jug1Capacity, jug2Capacity, targetCapacity
        if x > y: x, y = y, x
        if z > x + y: return False

        stack = [(0, 0)]
        seen = set()
        while stack:
            a, b = stack.pop()
            if (a, b) in seen: continue
            seen.add((a, b))

            if a == z or b == z or a + b == z: return True
            if not (0 <= a <= x and 0 <= b <= y): continue

            stack.append((x, b))
            stack.append((a, y))
            stack.append((a, 0))
            stack.append((0, b))

            if y - b >= a:
                stack.append((0, b + a))
            else:
                stack.append((a - y + b, y))

            if x - a >= b:
                stack.append((a + b, 0))
            else:
                stack.append((x, b - x + a))

        return False

import math
class Solution2:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        x, y, z = jug1Capacity, jug2Capacity, targetCapacity
        if z > x + y: return False

        return z % math.gcd(x, y) == 0