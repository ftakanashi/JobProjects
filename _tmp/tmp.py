class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        dp = [0 for _ in range(n + 1)]
        dp[0] = 1
        dp[1] = 9 if s[0] == '*' else 1
        MOD = 10**9 + 7
        for i in range(2, n+1):
            prev, ch = s[i-2], s[i-1]
            if ch == '*':
                dp[i] += (dp[i-1] * 9)
                if prev == '*':
                    dp[i] += (dp[i-2] * 15)
                elif prev == '0':
                    pass
                elif prev in '12':
                    if prev == '1': dp[i] += (dp[i-2] * 10)
                    else: dp[i] += (dp[i-2] * 7)

            else:
                if ch != '0':
                    dp[i] += dp[i-1]
                if prev == '*':
                    dp[i] += (dp[i-2] * (2 if ch <= '6' else 1))
                elif prev == '0':
                    pass
                elif int(prev+ch) <= 26:
                    dp[i] += dp[i-2]

            dp[i] %= MOD

        return dp[-1]

s = Solution()
s.numDecodings('**')