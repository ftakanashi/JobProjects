from typing import List

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        num2i = {}
        n = len(arr)
        dp = [1 for _ in range(n)]

        for i in range(n):
            num = arr[i]
            if num - difference in num2i:
                dp[i] = dp[num2i[num - difference]] + 1
            num2i[num] = i

        return max(dp)