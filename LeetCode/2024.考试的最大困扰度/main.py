#!/usr/bin/env python
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        n = len(answerKey)

        def helper(flag):    # 统计以 flag 为基准时最长连续片段的长度，此函数就是 LC.1004
            l = r = ans = 0
            rest = k
            while r < n:
                if answerKey[r] != flag: rest -= 1
                while l <= r and rest < 0:
                    if answerKey[l] != flag: rest += 1
                    l += 1
                ans = max(ans, r - l + 1)
                r += 1

            return ans

        return max(helper("T"), helper("F"))