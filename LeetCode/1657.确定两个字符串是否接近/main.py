#!/usr/bin/env python
# -*- coding:utf-8 -*-
from collections import Counter

class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2): return False
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        ch_counter1 = Counter(counter1.keys())
        times_counter1 = Counter(counter1.values())
        ch_counter2 = Counter(counter2.keys())
        times_counter2 = Counter(counter2.values())

        return ch_counter1 == ch_counter2 and times_counter1 == times_counter2