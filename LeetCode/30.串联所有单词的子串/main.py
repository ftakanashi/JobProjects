#!/usr/bin/env python

from typing import List

from collections import Counter

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:

        counter = Counter(words)
        w_len = len(words[0])
        sub_len = len(words) * w_len

        def search_from(start: int) -> List[int]:
            res = []
            l = r = start
            window = Counter()

            while r < len(s):
                span = s[r : r+w_len]
                window[span] += 1

                if span not in counter:
                    l = r = r + w_len
                    window = Counter()
                    continue
                    # 下面也是一种可行的办法，不过要挨个扫描单词，不如直接将l和r置值更快
                    # while window[span] > 0:
                    #     window[s[l : l+w_len]] -= 1
                    #     l += w_len

                elif window[span] > counter[span]:
                    while window[span] > counter[span]:
                        window[s[l : l+w_len]] -= 1
                        l += w_len

                r += w_len

                if r - l == sub_len:
                    res.append(l)
                    window[s[l : l+w_len]] -= 1
                    l += w_len

            return res

        total_res = []
        for i in range(w_len):
            subres = search_from(i)
            total_res.extend(subres)

        return total_res