from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) <= 1: return True
        count = 0
        i = 0
        while i < len(nums) - 1:
            if nums[i] > nums[i+1]:
                count += 1
                if count > 1: return False
                if i > 0 and nums[i+1] < nums[i-1]:
                    nums[i+1] = nums[i]
            i += 1
        return True