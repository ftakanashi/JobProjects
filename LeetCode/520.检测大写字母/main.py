#!/usr/bin/env python
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        all_up_flag = True
        last_up = 0
        for i, ch in enumerate(word):
            if ch.isupper():
                last_up = i
            else:
                all_up_flag = False
        return all_up_flag or last_up == 0