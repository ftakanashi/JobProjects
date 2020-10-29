#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        if len(s) < 2:
            return len(s)

        lookup = set([s[0], ])    # 窗口内字符集合
        # 因为总长度小于2的情况已经除外，所以可以直接left=0, right=1开始
        left, right = 0, 1
        max_len = 1

        while right < len(s):
            if s[right] in lookup:
                while s[left] != s[right]:
                    lookup.remove(s[left])
                    left += 1
                # 此时s[left]==s[right]，别忘了再让left += 1
                left += 1
                # 这条分支下（右边新进来的字符是重复字符），至少也是窗口整体右移一格，max_len不会增长
                # 所以不管max_len拉倒
            else:
                lookup.add(s[right])
                max_len = max(max_len, right - left + 1)

            right += 1

        return max_len