#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List, Union

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        wordSet = set(wordDict)
        cache = {}

        def dfs(n: int) -> Union[List[str], None]:
            '''
            返回s[n:]子串所有可能的分割方式组成的List
            如果已经到头就返回None
            '''

            if n == len(s):
                return

            if n in cache:
                return cache[n]

            i = n + 1
            res = []
            while i <= len(s):
                word = s[n:i]
                if word in wordSet:
                    suffix_patterns = dfs(i)
                    if suffix_patterns is None:    # 剩下刚好是word
                        res.append(word)
                    else:
                        for suffix_pattern in suffix_patterns:
                            res.append(word + ' ' + suffix_pattern)
                i += 1

            cache[n] = res
            return res

        return dfs(0)