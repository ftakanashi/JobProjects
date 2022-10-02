#!/usr/bin/env python
from typing import List

class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:

        n = len(code)
        if k == 0: return [0 for _ in range(n)]

        code = code + code

        presum = [0, ]
        for num in code:
            presum.append(presum[-1] + num)
        presum = presum[1:]

        ans = []
        pos = 0 if k > 0 else n
        for i in range(pos, pos + n):
            if k < 0:
                ans.append(presum[i - 1] - presum[i + k - 1])    # 注意这个分支中别忘了两边都要减去1
            else:
                ans.append(presum[i + k] - presum[i])
        return ans