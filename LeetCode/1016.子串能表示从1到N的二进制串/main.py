#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N+1):
            if bin(i)[2:] not in S:
                return False
        return True