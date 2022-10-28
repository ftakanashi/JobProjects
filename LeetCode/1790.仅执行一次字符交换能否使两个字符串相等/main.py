#!/usr/bin/env python
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        a1 = a2 = b1 = b2 = None
        for i, (ch1, ch2) in enumerate(zip(s1, s2)):
            if ch1 == ch2: continue
            if a1 is None:
                a1, b1 = ch1, ch2
            elif a2 is None:
                a2, b2 = ch1, ch2
            else:
                return False

        return a1 == b2 and a2 == b1    # 最终如此返回还可以囊括进两个字符串只有一个字符不同的情况