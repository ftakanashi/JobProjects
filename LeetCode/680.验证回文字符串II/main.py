#!/usr/bin/env python

class Solution:
    def validPalindrome(self, s: str) -> bool:

        flag = True

        def rec(i, j):
            nonlocal flag
            while i < j:
                if s[i] == s[j]:
                    i += 1
                    j -= 1
                    # 这里当然也可以是 return rec(i+1, j-1)，不过因为大部分扫描都是合法的，因此会创建大量递归栈。这里不如直接递推缩小范围。
                elif flag:
                    flag = False
                    return rec(i+1, j) or rec(i, j-1)
                else:
                    return False
            return True

        return rec(0, len(s)-1)