#!/usr/bin/env python
import string

digits = set("1234567890")
letters = set(string.ascii_lowercase)
puncs = set("!.,")
class Solution:
    def countValidWords(self, sentence: str) -> int:
        tokens = sentence.split()

        def check(token):
            hyphen = False
            for i, ch in enumerate(token):
                if ch == "-":
                    if hyphen: return False
                    if i == 0 or token[i-1] not in letters: return False
                    if i == len(token) - 1 or token[i+1] not in letters: return False
                    hyphen = True
                elif ch in puncs:
                    if i != len(token) - 1: return False
                elif ch in digits:
                    return False
            return True

        return list(map(check, tokens)).count(True)