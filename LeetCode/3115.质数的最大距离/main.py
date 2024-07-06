#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

import math
class Solution:
    def maximumPrimeDifference(self, nums: List[int]) -> int:

        def is_prime(n):
            if n < 2: return False
            for i in range(2, int(math.sqrt(n)) + 1):
                if n % i == 0: return False
            return True

        i, j = 0, len(nums) - 1
        while not is_prime(nums[i]):
            i += 1
        while not is_prime(nums[j]):
            j -= 1
        return j - i