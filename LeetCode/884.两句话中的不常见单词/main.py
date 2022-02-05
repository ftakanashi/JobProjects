#!/usr/bin/env python
from typing import List

from collections import Counter
class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        words = s1.split() + s2.split()
        counter = Counter(words)
        return [word for word in words if counter[word] == 1]