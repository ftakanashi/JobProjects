#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        words1 = sentence1.split()
        words2 = sentence2.split()
        if len(words1) < len(words2):
            words2, words1 = words1, words2

        m, n = len(words1), len(words2)

        i = j = 0
        while i < m and j < n and words1[i] == words2[j]:
            i += 1
            j += 1

        k, l = m - 1, n - 1
        while k >= 0 and l >= 0 and words1[k] == words2[l]:
            k -= 1
            l -= 1

        return j > l