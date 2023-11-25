#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        seen = {1, }
        curr, step = 1, k
        while True:
            curr = (curr + step) % n or n    # 如果余数是0，则说明传递到n号朋友手上
            step += k
            if curr in seen:
                break
            seen.add(curr)

        return [i for i in range(1, n + 1) if i not in seen]