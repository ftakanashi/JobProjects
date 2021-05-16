#!/usr/bin/env python

from typing import List

class Solution:
    def decode(self, encoded: List[int]) -> List[int]:
        n = len(encoded) + 1

        # perm总异或结果
        total = 0
        for k in range(n%4+1): total = total ^ (n-k)

        # 根据总异或结果求perm[0]
        start = total
        for i in range(1, len(encoded), 2): start = start ^ encoded[i]

        # 根据perm[0]求整个序列
        res = [start,]
        for i in range(len(encoded)):
            res.append(res[-1] ^ encoded[i])
        return res