#!/usr/bin/env python
class Solution1:
    def minSteps(self, n: int) -> int:
        dp = [i for i in range(n+1)]
        dp[1] = 0
        for i in range(1, n+1):
            for j in range(i//2, 1, -1):
                if (i - j) % j == 0:
                    dp[i] = min(dp[i], dp[j] + ((i-j) // j) + 1)
                    break

        return dp[-1]

class Solution2:
    def minSteps(self, n: int) -> int:
        ans = 0
        i = 2
        while i * i <= n:
            while n % i == 0:
                n //= i
                ans += i
            i += 1

        if n > 1:
            ans += n

        return ans