#!/usr/bin/env python
# -*- coding:utf-8 -*-
from typing import List

class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        n = len(s)

        def check(word):
            """
            检查某个单词是否能按题意扩张为s
            """
            i = j = 0
            m = len(word)
            if m > n: return False
            while i < n and j < m:
                if s[i] != word[j]: return False
                c1 = c2 = 1
                # 指针指向两边字符相同时，先后移动i和j
                # 将两边相同的一片字母都先遍历完，并且用c1和c2进行计数
                while i < n - 1 and s[i + 1] == word[j]:
                    i += 1
                    c1 += 1
                while j < m - 1 and s[i] == word[j + 1]:
                    j += 1
                    c2 += 1

                # 按分类讨论情况，符合下面条件的是要直接否决的
                if c1 < c2 or (c1 > c2 and c1 < 3): return False
                i += 1
                j += 1

            # 遍历完成后，只有i指针走完了整个s才是符合条件的情况
            return i >= n

        ans = 0
        for word in words:
            if check(word): ans += 1
        return ans