#!/usr/bin/env python

from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        ans = []
        chmap = {}
        for ch in 'qwertyuiop': chmap[ch] = 0
        for ch in 'asdfghjkl': chmap[ch] = 1
        for ch in 'zxcvbnm': chmap[ch] = 2

        for word in words:
            row = chmap[word[0].lower()]
            flag = True
            for ch in word[1:]:
                if chmap[ch.lower()] != row: flag = False
            if flag:
                ans.append(word)
        return ans