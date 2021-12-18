#!/usr/bin/env python
from typing import List

from collections import defaultdict
class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbr2word = defaultdict(set)
        for word in dictionary:
            abbr = self.getAbbr(word)
            self.abbr2word[abbr].add(word)

    def isUnique(self, word: str) -> bool:
        abbr = self.getAbbr(word)
        if len(self.abbr2word[abbr]) == 0:
            return True
        elif len(self.abbr2word[abbr]) == 1:
            return word == list(self.abbr2word[abbr])[0]
        return False

    def getAbbr(self, word: str) -> str:
        n = len(word)
        if n <= 2: return word
        return word[0] + str(n - 2) + word[-1]


# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)