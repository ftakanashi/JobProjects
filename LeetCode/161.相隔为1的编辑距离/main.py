#!/usr/bin/env python
class Solution:
    def check(self, s:str, t:str) -> bool:    # 双指针判断两个长度差1的字符串是否编辑距离是1
        m, n = len(s), len(t)
        # assert m > n    # 此函数需要保证s长度大于t
        i = j = 0
        flag = True
        while i < m and j < n:
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                if not flag: return False
                flag = False
                i += 1
        return True

    def isOneEditDistance(self, s: str, t: str) -> bool:
        m, n = len(s), len(t)
        if m == n:
            flag = True
            for i in range(n):
                if s[i] != t[i]:
                    if flag: flag = False
                    else: return False
            return not flag    # 注意完全相同时，此时flag还是True，但这是我们要排除的情况。
        elif m == n - 1:
            return self.check(t, s)
        elif m - 1 == n:
            return self.check(s, t)
        else:
            return False