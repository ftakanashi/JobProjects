#!/usr/bin/env python
class Solution1:
    def longestSubstring(self, s: str, k: int) -> int:
        max_len = 0
        for type_num in range(1, 27):
            if type_num * k > len(s): break
            res = self.slide(type_num, s, k)
            max_len = max(max_len, res)
        return max_len

    def slide(self, type_num, s, k):
        l, r = 0, 0
        counter = {}
        save_count = 0
        max_len = 0
        while r < len(s):
            ch = s[r]
            if ch not in counter:
                counter[ch] = 0
            counter[ch] += 1
            if counter[ch] == k: save_count += 1

            if len(counter) == type_num and save_count == type_num:
                # len(counter) == type_num表示窗口内恰好有type_num种字符
                # save_count == type_num表示窗口中每一种字符都满足计数大于等于k
                max_len = max(max_len, r - l + 1)

            while l < r and len(counter) > type_num:
                ch = s[l]
                if counter[ch] == k: save_count -= 1
                counter[ch] -= 1
                if counter[ch] == 0: del counter[ch]
                l += 1

            r += 1

        return max_len

import collections
class Solution2:
    def longestSubstring(self, s: str, k: int) -> int:

        def rec(sub: str):
            if not sub: return 0
            counter = collections.Counter(sub)
            for ch in counter:
                if counter[ch] < k:
                    return max([rec(subsub) for subsub in sub.split(ch)])
            return len(sub)

        return rec(s)