from typing import List

def findDuplicates(nums: List[int]) -> List[int]:
    i = 0
    res = set()
    while i < len(nums):
        if nums[i] != i + 1:
            if nums[nums[i] - 1] == nums[i]:
                res.add(nums[i])
                i += 1
            else:
                tmp1, tmp2 = nums[i], nums[nums[i] - 1]
                nums[i], nums[tmp1 - 1] = tmp2, tmp1
        else:
            i += 1
    return res

print(findDuplicates([4,3,2,7,8,2,3,1]))