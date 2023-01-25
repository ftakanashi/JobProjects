#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        # 使用 max_v, rest 分别表示最大值和较小的两个值的和，这样就可以不用排一次序了
        s = sum([a, b, c])
        max_v = max([a, b, c])
        rest = s - max_v
        return rest if rest <= max_v else max_v + rest // 2