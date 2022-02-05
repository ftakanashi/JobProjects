#!/usr/bin/env python
class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        max_start, max_len = -1, 0

        def dfs(start, end):
            nonlocal max_start, max_len
            if start >= end: return ""

            # 将片段中的字母出现情况维护到两个flag变量中
            lower = upper = 0
            for i in range(start, end + 1):
                if s[i].islower():
                    lower |= (1 << (ord(s[i]) - ord("a")))
                else:
                    upper |= (1 << (ord(s[i]) - ord("A")))

            if upper == lower:    # 若两者相等，说明片段中所有字母都配对，片段本身是一个美好字符串
                if end - start + 1 > max_len:
                    max_len = end - start + 1
                    max_start = start
                return

            # 若走到这里，说明片段中有害群之马，需要将其扫描出来，并进一步探索那些不包含害群之马的子串
            prev = start    # README中提到的优化点，不是暴力地扫描害群之马的两边，而是动态维护一个不断前进的左边界
            for i in range(start, end + 1):
                idx = ord(s[i].lower()) - ord("a")
                if (s[i].islower() and upper & (1 << idx) == 0) \
                        or (s[i].isupper() and lower & (1 << idx) == 0):
                    # s[i]是害群之马
                    dfs(prev, i - 1)
                    prev = i + 1
            dfs(prev, end)    # 最后别忘了，prev到end这一段很有可能还没被扫描呢

        dfs(0, len(s) - 1)
        return s[max_start : max_start + max_len] if max_len > 0 else ""