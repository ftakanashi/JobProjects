#!/usr/bin/env python

'''
# 初步废案：
class Solution:
    def longestDupSubstring(self, s: str) -> str:

        def check(m):
            char_codes = [ord(ch) - ord('a') for ch in s]
            seen, code = set(), 0
            for i in range(m):
                code = code * 26 + char_codes[i]
            seen.add(code)

            for i in range(m, len(s)):
                code = (code - char_codes[i-m] * (26 ** (m-1))) * 26 + char_codes[i]
                if code in seen: return i
                seen.add(code)

            return -1

        s_len = len(s)
        l, r = 0, s_len - 1
        ans = [-1, 0]
        while l <= r:
            mid = (l + r) // 2
            pos = check(mid)
            if pos < 0:
                r = mid - 1
            else:
                ans = [pos, mid]
                l = mid + 1

        pos, leng = ans
        return s[pos - leng + 1 : pos + 1] if pos > 0 else ''
'''

from random import randint
class Solution:
    def longestDupSubstring(self, s: str) -> str:
        char_codes = [ord(ch) - ord('a') for ch in s]    # 实现将所有字符的单个位的编码算出来
        base1, base2 = randint(26, 100), randint(26, 100)    # 定义两个进制
        mod1, mod2 = randint(10**9+7, 2**31-1), randint(10**9+7, 2**31-1)    # 定义两个进制各自的模

        def check(m):    # 检查长度为m的子串是否有重复的，若有返回第一个发现的重复子串的末尾位置，无则返回-1
            seen = set()
            code1 = code2 = 0
            for i in range(m):
                code1 = (code1 * base1 + char_codes[i]) % mod1
                code2 = (code2 * base2 + char_codes[i]) % mod2
            seen.add((code1, code2))    # 计算s[:m]子串的编码，入哈希集

            diff1 = pow(base1, m-1, mod1)    # 滑窗过程中减去最高位时乘的系数
            diff2 = pow(base2, m-1, mod2)
            for i in range(m, len(s)):    # 遍历所有长度为m的子串
                code1 = ((code1 - char_codes[i-m] * diff1) * base1 + char_codes[i]) % mod1
                code2 = ((code2 - char_codes[i-m] * diff2) * base2 + char_codes[i]) % mod2
                if (code1, code2) in seen: return i    # 若某个子串的编码已经出现在哈希集中，说明子串有重复
                seen.add((code1, code2))
            return -1

        s_len = len(s)
        l, r = 0, s_len - 1
        ans = [-1, 0]    # 用于收集答案
        while l <= r:
            mid = (l + r) // 2
            pos = check(mid)
            if pos < 0:    # 说明所有长度为mid的子串都没有重复
                r = mid - 1
            else:    # 有重复
                ans = [pos, mid]    # 为了防止下一轮二分可能会走出有重复子串你的长度的区域，应该及时记录下来
                l = mid + 1

        pos, leng = ans
        return s[pos - leng + 1 : pos + 1] if pos > 0 else ''