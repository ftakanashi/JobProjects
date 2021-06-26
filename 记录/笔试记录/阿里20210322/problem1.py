  #!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys

def process(n, m, weights):
    dp = [[False for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n + 1): dp[i][0] = True
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if dp[i-1][j]:
                dp[i][j] = True
            elif j - weights[i-1] >= 0 and dp[i-1][j - weights[i-1]]:
                dp[i][j] = True

    return dp[-1][-1]

def main():
    print(process(3, 200, [100, 120, 120]))

if __name__ == '__main__':
    main()