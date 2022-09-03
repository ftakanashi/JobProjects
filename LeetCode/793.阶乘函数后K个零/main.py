#!/usr/bin/env python
import bisect

class Solution:
    def preimageSizeFZF(self, k: int) -> int:
        def count_zero(num):
            cnt = 0
            while num:
                num = num // 5
                cnt += num
            return cnt

        def search(tgt):
            return bisect.bisect_left(range(5 * tgt), tgt, key=count_zero)

        return search(k + 1) - search(k)