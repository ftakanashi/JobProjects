from typing import List
from collections import Counter

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        s = ans = 0
        counter = Counter([0,])
        for num in nums:
            s += num
            if goal - s in counter:
                ans += counter[goal - s]
                print(s, goal-s)
            counter[s] += 1
        return ans

if __name__ == '__main__':
    s = Solution()
    res = s.numSubarraysWithSum([1,0,1,0,1], 2)
    print(res)