#!/usr/bin/env python
from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {ch: i for i, ch in enumerate(order)}
        encoded = [tuple(order_dict[ch] for ch in word) for word in words]
        for i in range(1, len(words)):
            if encoded[i-1] > encoded[i]: return False
        return True