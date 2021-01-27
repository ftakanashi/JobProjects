#!/usr/bin/env python

class Solution1:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        while n > 1:
            if n % 3 != 0:
                return False
            n = n // 3
        return True

import math
class Solution2:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0: return False
        power = math.log(n, 3)
        if power == int(power) or abs(power - (int(power) + 1)) < 1e-10:
            return True

        return False