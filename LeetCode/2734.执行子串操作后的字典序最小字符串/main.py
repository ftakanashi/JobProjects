#!/usr/bin/env python
# -*- coding:utf-8 -*-

class Solution:
    def smallestString(self, s: str) -> str:
        i, j, n = 0, 0, len(s)
        # 跳过开头连续a
        while i < n and s[i] == 'a':
            i += 1
        if i == n: i = n - 1    # 全是a的情况
        j = i + 1
        while j < n and s[j] != 'a':
            j += 1

        return s[:i] + "".join([chr(ord(ch) - 1) if ch != 'a' else 'z' for ch in s[i:j]]) + s[j:]