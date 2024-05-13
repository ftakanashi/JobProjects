#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List
from collections import defaultdict

class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        inbound = defaultdict(int)
        for a, b in edges:
            inbound[b] += 1

        champ = None
        for node in range(n):
            if inbound[node] == 0:
                if champ is None:
                    champ = node
                else:
                    return -1
        return champ
