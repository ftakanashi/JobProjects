#!/usr/bin/env python
# -*- coding:utf-8 -*-

def calc_cost(s, t, switch_cost, flip_cost):
    n = len(s)
    dp = [0 for _ in range(n)]
    i = 1
    if s[0] != t[0]:
        if s[1] == t[0] and t[1] == s[0]:
            dp[0] = dp[1] = min(switch_cost, 2*flip_cost)
            i = 2
        else:
            dp[0] = flip_cost

    while i < n:
        if s[i] == t[i]:
            dp[i] = dp[i-1]
        elif i < n - 1 and s[i] == t[i+1] and t[i] == s[i+1]:
            dp[i] = dp[i+1] = dp[i-1] + min(switch_cost, 2*flip_cost)
            i += 1
        else:
            dp[i] = dp[i-1] + flip_cost
        i += 1

    return dp[-1]

if __name__ == '__main__':
    s = 'abababbababa'
    t = 'bbabababbbba'
    print(calc_cost(s, t, 5, 1))