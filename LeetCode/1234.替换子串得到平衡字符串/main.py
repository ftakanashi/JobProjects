#!/usr/bin/env python
# -*- coding:utf-8 -*-

from collections import Counter

class Solution:
    def balancedString(self, s: str) -> int:
        cnt = Counter(s)
        std = len(s) // 4
        window = Counter()    # 维护窗口中各个字符的计数

        def check():    # 检查当前窗口是否合法，即替换当前窗口对应的子串，能否得到均衡字符串
            for ch in "QWER":
                if window[ch] < cnt[ch] - std:    # 要求就是每个字符的计数值都大于等于其要从原串中去掉的个数
                    return False
            return True

        if check(): return 0

        ans = len(s)
        l = r = 0

        # 开始滑窗
        # 这里，滑窗采用了经典的模板思路。即先尽可能拓宽右边界，然后在符合条件的情况下收缩左边界
        # 和模板有所不同的是收割答案的位置、维护窗口状态量的位置
        while r < len(s):
            window[s[r]] += 1

            while l <= r and check():
                ans = min(ans, r - l + 1)
                window[s[l]] -= 1
                l += 1

            r += 1

        return ans