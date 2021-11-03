#!/usr/bin/env python

class Solution1:
    def reorderedPowerOf2(self, n: int) -> bool:
        nums = list(str(n))
        end = len(nums)
        check = lambda x:(x & (x-1)) == 0

        def dfs(pos):
            s = ''.join(nums)
            if s.startswith('0'): return False
            if check(int(s)): return True
            if pos == end-1: return False

            # 基于交换进行全排列枚举。增设seen避免相同数字交换到同一位置引起重复计算
            seen = set()
            for i in range(pos, end):
                if nums[i] in seen: continue
                seen.add(nums[i])
                nums[pos], nums[i] = nums[i], nums[pos]
                flag = dfs(pos + 1)
                nums[pos], nums[i] = nums[i], nums[pos]
                if flag: return True
            return False

        return dfs(0)

from collections import Counter
class Solution2:
    def reorderedPowerOf2(self, n: int) -> bool:

        def num2tuple(num):
            counter = Counter(str(num))
            res = tuple([counter[str(i)] for i in range(10)])
            return res

        counters = set()
        base = 1
        while base < 10**9:
            counters.add(num2tuple(base))
            base *= 2

        query = num2tuple(n)
        return query in counters