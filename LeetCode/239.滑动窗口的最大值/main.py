#!/usr/bin/env python
from typing import List

import collections
import heapq

class Solution1:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        heap = [(-n, i) for i, n in enumerate(nums[:k])]
        heapq.heapify(heap)
        res = [-heap[0][0]]
        i, j = 1, k
        while j < len(nums):
            heapq.heappush(heap, (-nums[j], j))
            while heap[0][1] < i:
                heapq.heappop(heap)
            res.append(-heap[0][0])
            i += 1
            j += 1

        return res


class Solution2:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = collections.deque([ (nums[0], 0) ])
        for i in range(1, k):
            while len(q) > 0 and q[-1][0] < nums[i]:
                q.pop()
            q.append( (nums[i], i) )

        res = [q[0][0], ]
        for i in range(k, len(nums)):
            while len(q) > 0 and q[-1][0] < nums[i]:
                q.pop()
            q.append( (nums[i], i) )

            while len(q) > 0 and q[0][1] <= i - k:
                q.popleft()
            res.append(q[0][0])

        return res
