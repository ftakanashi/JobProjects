#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def kSimilarity(self, s1: str, s2: str) -> int:

        times, n, q, seen = 0, len(s1), [(s1, 0)], set([s1, ])

        while q:
            new_q = []
            for s, i in q:
                if s == s2: return times

                while i < n and s[i] == s2[i]:
                    i += 1

                for j in range(i + 1, n):
                    if s[j] != s2[i]: continue
                    t = list(s)
                    t[i], t[j] = t[j], t[i]
                    t = ''.join(t)
                    if t not in seen:
                        seen.add(t)
                        new_q.append((t, i + 1))

            q = new_q
            times += 1    # 每进入一次循环，其实都是一次对中间状态推进的一步，所以直接times += 1即可

        return times