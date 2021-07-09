#!/usr/bin/env python
class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        counter = Counter(deliciousness)
        cands = list(counter.keys())
        n = len(cands)
        ans = 0

        for i in range(n):
            # for p in range(22):
            # rest = 2**p - cands[i]
            # if rest < 0: continue
            # if rest > cands[i]: break
            # if rest in counter:
            #     if rest == cands[i]:
            #         ans += (counter[rest] * (counter[rest] - 1) // 2)
            #     else:
            #         ans += (counter[rest] * counter[cands[i]])

            for p in range(21, -1, -1):
                rest = 2**p - cands[i]
                if rest < cands[i]: break
                if rest in counter:
                    if rest == cands[i]:
                        ans += (counter[rest] * (counter[rest] - 1) // 2)
                    else:
                        ans += (counter[rest] * counter[cands[i]])
                    ans = ans % (10**9 + 7)
        return ans