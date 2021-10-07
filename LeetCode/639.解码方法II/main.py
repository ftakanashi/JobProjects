#!/usr/bin/env python

class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        MOD = 10**9 + 7

        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        if s[0] == '*': dp[1] = 9    # 根据不同情况进行dp[1]的初始化
        elif s[0] != '0': dp[1] = 1
        else: return 0

        for i in range(2, n+1):
            prev, ch = s[i-2], s[i-1]
            if ch == '*':
                dp[i] += (dp[i-1] * 9)    # 当前字符是通配符的单分片情况
                if prev == '*':
                    dp[i] += (dp[i-2] * 15)    # 当前字符和前一个都是通配符的双分片，这里的系数15是指11-19，21-26这15个数字（题设提到了，通配符不表示0
                elif prev == '0':
                    pass    # 这个分支可以不显式写出，这里姑且写上
                elif prev in '12':
                    if prev == '1': dp[i] += (dp[i-2] * 9)    # 11-19
                    else: dp[i] += (dp[i-2] * 6)    # 21-26

            else:
                if ch != '0':    # 若当前字符是0，则无单分片情况
                    dp[i] += dp[i-1]
                if prev == '*':
                    dp[i] += (dp[i-2] * (2 if ch <= '6' else 1))    # 若上个字符是通配，当前字符必须是0-6间的才能通配出两种可能，否则仅一种可能
                elif prev == '0':
                    pass
                elif int(prev+ch) <= 26:
                    dp[i] += dp[i-2]    # 上个字符和当前字符都是普通数字字符（上个字符不为0），那么就退化成LC.91的情况，直接递推即可

            dp[i] %= MOD

        return dp[-1]