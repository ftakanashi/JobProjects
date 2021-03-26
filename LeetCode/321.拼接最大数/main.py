#!/usr/bin/env python

from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:

        def pick(nums, keep):
            if keep == 0: return []    # 选取0个，即直接返回空列表

            # 选取个数大于长度，即全选。注意不要返回原引用。因为pick后续的merge会对结果数组进行编辑，如果返回原引用则直接编辑了原数组。
            if keep >= len(nums): return nums.copy()

            stack = []
            drop = len(nums) - keep
            for n in nums:
                while drop > 0 and stack and n > stack[-1]:
                    stack.pop()
                    drop -= 1
                stack.append(n)
            return stack[:keep]

        def merge(res1, res2):
            res = []
            while res1 or res2:
                bigger = res1 if res1 > res2 else res2
                res.append(bigger.pop(0))
            return res

        ans = []
        for p in range(k+1):
            if p <= len(nums1) and (k - p) <= len(nums2):
                r1 = pick(nums1, p)
                r2 = pick(nums2, k - p)
                r = merge(r1, r2)
                if r > ans: ans = r    # 这里也直接用列表间大小比较即可。换言之Python的列表比较机制，恰好适合这种字典序的比较。
        return ans