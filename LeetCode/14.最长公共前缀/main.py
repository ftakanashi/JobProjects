#!/usr/bin/env python

from typing import List

class Solution1:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def rec(i: int):
            ch = strs[0][i]
            for n in range(1, len(strs)):
                s = strs[n]
                if s[i] != ch:
                    return False, ''
            return True, ch

        if len(strs) == 0: return ''

        min_len = min([len(s) for s in strs])
        res = ''
        for i in range(min_len):
            flag, ch = rec(i)
            if flag: res += ch
            else:
                break

        return res

class Solution2:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        def lcp(left: int, right: int) -> str:
            if left == right:
                return strs[left]

            mid = (left + right) // 2
            left_lcp = lcp(left, mid)
            right_lcp = lcp(mid + 1, right)

            i = 0
            while i < min(len(left_lcp), len(right_lcp)) and left_lcp[i] == right_lcp[i]:
                i += 1

            return left_lcp[:i]

        if len(strs) == 0: return ''
        return lcp(0, len(strs) - 1)