#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def findReplaceString(self, s: str, indices: List[int], sources: List[str], targets: List[str]) -> str:
        s_list = list(s)
        for i, src, tgt in zip(indices, sources, targets):
            if s[i: i + len(src)] == src:
                for j in range(i, i + len(src)):
                    s_list[j] = ""
                s_list[i] = tgt

        return "".join(s_list)