#!/usr/bin/env python
# -*- coding:utf-8 -*-

import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        cand = math.sqrt((n**2 + n) / 2)
        if int(cand) == cand:
            return int(cand)
        else:
            return -1