#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordSet = set(wordDict)

        def dfs(n: int, prefix: str, totalRes: List):

            if n == len(s):
                totalRes.append(prefix.strip())
                return

            i = n + 1
            while i <= len(s):
                word = s[n:i]
                if word in wordSet:
                    new_prefix = prefix + word + ' '
                    dfs(i, new_prefix, totalRes)

                i += 1

        total_res = []
        dfs(0, '', total_res)

        return total_res