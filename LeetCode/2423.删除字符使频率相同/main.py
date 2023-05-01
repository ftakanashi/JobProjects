#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        counter = Counter(word)
        for ch in word:
            counter[ch] -= 1
            if counter[ch] == 0:
                counter.pop(ch)
            if len(set(counter.values())) == 1:
                return True
            counter[ch] += 1
        return False