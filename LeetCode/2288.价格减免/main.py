#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def discountPrices(self, sentence: str, discount: int) -> str:
        ans = []
        for word in sentence.strip().split():
            if word.startswith("$") and word[1:].isdigit():
                val = int(word[1:]) * ((100 - discount) / 100.0)
                ans.append("${:.2f}".format(val))
            else:
                ans.append(word)
        return " ".join(ans)