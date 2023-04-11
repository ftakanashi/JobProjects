#!/usr/bin/env python
# -*- coding:utf-8 -*-

from typing import List, Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        nums = []
        p = head
        while p is not None:
            nums.append(p.val)
            p = p.next

        stack = []
        n = len(nums)
        ans = []
        for i in range(n - 1, -1, -1):

            while stack and nums[stack[-1]] <= nums[i]:
                stack.pop()

            ans.append(n if len(stack) == 0 else stack[-1])
            stack.append(i)

        ans.reverse()
        return [nums[i] if i < n else 0 for i in ans]