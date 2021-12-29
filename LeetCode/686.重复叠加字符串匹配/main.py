#!/usr/bin/env python
class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        len_a, len_b = len(a), len(b)
        # 可以过滤掉的一些情况
        if len_a >= len_b:
            if a.find(b) != -1: return 1
            elif (a*2).find(b) != -1: return 2
            else: return -1
        if set(a) != set(b): return -1

        # 先算可能的k
        possible_cnt = [len_b // len_a + 1]
        if len_b % len_a == 0:
            possible_cnt.insert(0, len_b // len_a)
        elif len_b % len_a != 1:
            possible_cnt.append(len_b // len_a + 2)

        # 依次检查k
        for cnt in possible_cnt:
            ext_a = a * cnt
            if ext_a.find(b) != -1:
                return cnt
        return -1