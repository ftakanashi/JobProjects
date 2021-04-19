#!/usr/bin/env python

from typing import List
import bisect

class Solution1:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:
        if len(nums) <= 1 or k == 0: return False

        def f(a, b):
            return abs(a - b) <= t

        window = [nums[0],]
        for r in range(1, min(len(nums), k+1)):
            p = bisect.bisect_left(window, nums[r])
            if f(nums[r], window[p-1]) or (p < len(window) and f(nums[r], window[p])):
                return True
            window.insert(p, nums[r])

        l, r = 0, k + 1
        while r < len(nums):
            p = bisect.bisect_left(window, nums[l])
            window.pop(p)
            p = bisect.bisect_left(window, nums[r])
            if f(nums[r], window[p-1]) or (p < len(window) and f(nums[r], window[p])):
                return True

            window.insert(p, nums[r])
            l += 1
            r += 1

        return False


class Solution2:
    def containsNearbyAlmostDuplicate(self, nums: List[int], k: int, t: int) -> bool:

        def f(a, b): return abs(a - b) <= t

        buckets = {}
        for n in nums[:k+1]:
            bi = n // (t+1)
            # 当下列两种情况中的一种发生时，说明存在符合要求的两个下标，因此返回True
            # 两种情况分别是1.同桶内差值 <= t，2.相邻桶间差值 <= t
            if bi in buckets: return True
            if (bi - 1 in buckets and f(n, buckets[bi-1])) or (bi + 1 in buckets and f(n, buckets[bi+1])):
                return True
            buckets[bi] = n

        l, r = 0, k + 1
        while r < len(nums):
            # 滑动时删除左边界的桶
            bi = nums[l] // (t+1)
            buckets.pop(bi)

            # 和上面第一次遍历前k个元素一样的逻辑
            bi = nums[r] // (t+1)
            if bi in buckets: return True
            if (bi - 1 in buckets and f(nums[r], buckets[bi-1])) or (bi + 1 in buckets and f(nums[r], buckets[bi+1])):
                return True
            buckets[bi] = nums[r]

            l += 1
            r += 1

        return False