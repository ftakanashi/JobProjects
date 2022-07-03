#!/usr/bin/env python

class Solution:
    def magicalString(self, n: int) -> int:
        s = "122"    # 不要问为什么从这个前缀开始…从122开始程序写的比较顺手
        i = 2
        curr = "1"    # 表示当前要append的数字是1还是2
        ans = 1
        while len(s) < n:
            if s[i] == "1":
                s += curr
                if curr == "1": ans += 1
            else:
                s += curr * 2
                if curr == "1": ans += 2
            curr = "2" if curr == "1" else "1"
            i += 1
        if len(s) == n+1 and s[-1] == "1": ans -= 1    # 此时s可能长度是n+1，若此时恰好末尾是1，那么就要减去一
        return ans