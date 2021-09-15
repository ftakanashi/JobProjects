#!/usr/bin/env python
'''
本题代码未经系统检验，仅供参考
'''
import heapq

def process(n, nums):
    heap = []
    ans = 0
    happy = 0
    for num in nums:
        happy += num
        heapq.heappush(heap, num)
        ans = max(ans, len(heap))
        while happy < 0 and heap:
            cand = heapq.heappop(heap)
            happy -= cand
    return ans

def main():
    n = int(input().strip())
    nums = [int(num) for num in input().strip().split()]
    res = process(n, nums)
    print(res)

main()