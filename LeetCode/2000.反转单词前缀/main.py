#!/usr/bin/env python

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        word = list(word)
        j = 0
        while j < len(word):
            if word[j] == ch:
                break
            j += 1

        i = 0
        while j < len(word) and i < j:
            tmp = word[i]
            word[i] = word[j]
            word[j] = tmp
            i += 1
            j -= 1
        return "".join(word)